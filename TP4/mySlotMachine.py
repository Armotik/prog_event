import sys
from PyQt5.QtCore import QTimer, QRect, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFrame, QMainWindow, QApplication
import MyComponents.MyWidget_exo4 as exo4
import random

class mySlotMachineWidget(QFrame):
    def __init__(self, *args):
        super(mySlotMachineWidget, self).__init__(*args)
        self.setGeometry(0, 0, 800, 600)

        # Création de l'interface utilisateur
        self.ui = exo4.Ui_Form()
        self.ui.setupUi(self)

        self.bigimage = QPixmap("slot_machine_symbols.png")
        self.rect = QRect(0, 0, 300, 300)
        self.cropped = self.bigimage.copy(self.rect)

        self.ui.mLabel1.setPixmap(self.cropped)
        self.ui.mLabel2.setPixmap(self.cropped)
        self.ui.mLabel3.setPixmap(self.cropped)

        # Center the images in the QLabel widgets
        self.ui.mLabel1.setAlignment(Qt.AlignCenter)
        self.ui.mLabel2.setAlignment(Qt.AlignCenter)
        self.ui.mLabel3.setAlignment(Qt.AlignCenter)

        self.timer1 = QTimer()
        self.timer2 = QTimer()
        self.timer3 = QTimer()

        self.timer1.timeout.connect(self.updateLabel1)
        self.timer2.timeout.connect(self.updateLabel2)
        self.timer3.timeout.connect(self.updateLabel3)

    def Spin(self):
        self.timer1.start(100)
        self.timer2.start(100)
        self.timer3.start(100)
        QTimer.singleShot(1000, self.timer1.stop)
        QTimer.singleShot(1000, self.timer2.start)
        QTimer.singleShot(2000, self.timer2.stop)
        QTimer.singleShot(2000, self.timer3.start)
        QTimer.singleShot(3000, self.timer3.stop)

    def updateLabel1(self):
        self.updateLabel(self.ui.mLabel1)

    def updateLabel2(self):
        self.updateLabel(self.ui.mLabel2)

    def updateLabel3(self):
        self.updateLabel(self.ui.mLabel3)

    def updateLabel(self, label):
        x = random.choice([0, 300, 600])
        y = random.choice([0, 300, 600])
        self.rect.moveTo(x, y)
        self.cropped = self.bigimage.copy(self.rect).scaled(label.width(), label.height())
        label.setPixmap(self.cropped)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_S:
            self.Spin()

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setGeometry(100, 100, 1000, 800)
        self.setWindowTitle('Slot Machine Simulator')

        self.mDisplay = mySlotMachineWidget(self)
        self.setCentralWidget(self.mDisplay)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    sys.exit(app.exec_())