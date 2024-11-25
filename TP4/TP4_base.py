import sys

from PyQt5.QtCore import QTimer, QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import os

import MyComponents.MyWidget_exo4 as exo4


class MyImageViewerWidget(QFrame):

    def __init__(self, *args):

        super(MyImageViewerWidget, self).__init__(*args)
        self.setGeometry(0, 0, 800, 600)

        # Création de l'interface utilisateur
        self.ui = exo4.Ui_Form()
        self.ui.setupUi(self)
        self.img_list = []
        self.current_img = 0
        self.path = ""

        self.ui.mLabel1.setFixedWidth(300)
        self.ui.mLabel1.setFixedHeight(300)

        self.ui.mLabel2.setFixedWidth(300)
        self.ui.mLabel2.setFixedHeight(300)

        self.ui.mLabel3.setFixedWidth(300)
        self.ui.mLabel3.setFixedHeight(300)

        self.bigimage = QPixmap("slot_machine_symbols.png")
        self.rect = QRect(0, 0, 300, 300)
        self.cropped = self.bigimage.copy(self.rect)

        self.ui.mLabel1.setPixmap(self.cropped)
        self.ui.mLabel2.setPixmap(self.cropped)
        self.ui.mLabel3.setPixmap(self.cropped)

    # def LoadFiles(self):
    #     print("Loading files...")
    #     # self.path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
    #
    #     if self.path:
    #         print("Selected path: ", self.path)
    #
    #         for file in os.listdir(self.path):
    #             if file.endswith(".jpg") or file.endswith(".png"):
    #                 self.img_list.append(os.path.join(self.path, file))
    #
    #         self.img_list.sort()
    #         self.ui.mLineEdit.setText(self.path)
    #
    #         if len(self.img_list) > 0:
    #
    #             self.ui.mLabel.setPixmap(QPixmap(self.img_list[self.current_img]).scaled(self.ui.mLabel.width(), self.ui.mLabel.height()))
    #             self.ui.mLineEdit.setText(self.path + "/" + os.path.basename(self.img_list[self.current_img]))
    #     else:
    #         print("No path selected")

    def Next(self):
        print("Next image")

        x = self.rect.x()
        y = self.rect.y()

        if x + 300 < self.bigimage.width():
            self.rect.translate(300, 0)
            self.cropped = self.bigimage.copy(self.rect)

            self.ui.mLabel1.setPixmap(self.cropped)
            self.ui.mLabel2.setPixmap(self.cropped)
            self.ui.mLabel3.setPixmap(self.cropped)

        elif y + 300 < self.bigimage.height():
            self.rect.translate(-x, 300)
            self.cropped = self.bigimage.copy(self.rect)

            self.ui.mLabel1.setPixmap(self.cropped)
            self.ui.mLabel2.setPixmap(self.cropped)
            self.ui.mLabel3.setPixmap(self.cropped)

        else:
            self.rect.moveTo(0, 0)
            self.cropped = self.bigimage.copy(self.rect)

            self.ui.mLabel1.setPixmap(self.cropped)
            self.ui.mLabel2.setPixmap(self.cropped)
            self.ui.mLabel3.setPixmap(self.cropped)

    def Spin(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.Next)
        self.timer.start(1000 // 5)  # 5 images per second

        QTimer.singleShot(3000, self.timer.stop)

    def keyReleaseEvent(self, a0, QKeyEvent=None):
        if a0.key() == Qt.Key_S:
            self.Spin()

# def Previous(self):
#     print("Previous image")
#
#     if len(self.img_list) > 0:
#         self.current_img -= 1
#
#         if self.current_img < 0:
#             self.current_img = len(self.img_list) - 1
#
#         self.ui.mLabel.setPixmap(QPixmap(self.img_list[self.current_img]).scaled(self.ui.mLabel.width(), self.ui.mLabel.height()))
#         self.ui.mLineEdit.setText(self.path + "/" + os.path.basename(self.img_list[self.current_img]))
#
#     else:
#
#         x = self.rect.x()
#         y = self.rect.y()
#
#         if x - 300 >= 0:
#             self.rect.translate(-300, 0)
#             self.cropped = self.bigimage.copy(self.rect)
#
#             self.ui.mLabel.setPixmap(self.cropped)
#
#         elif y - 300 >= 0:
#             self.rect.translate(-x, -300)
#             self.cropped = self.bigimage.copy(self.rect)
#
#             self.ui.mLabel.setPixmap(self.cropped)
#
#         else:
#             self.rect.moveTo(self.bigimage.width() - 300, self.bigimage.height() - 300)
#             self.cropped = self.bigimage.copy(self.rect)
#
#             self.ui.mLabel.setPixmap(self.cropped)



class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        # attributs de la fenetre principale
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('Simple diaporama application')

        # donnée membre qui contiendra la frame associée à la widget crée par QtDesigner
        self.mDisplay = MyImageViewerWidget(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()
