import sys
from datetime import datetime

from PyQt5.QtGui import QPixmap, QColor, QPainter, QTransform
from PyQt5.QtWidgets import *


def GenerateSyracusSequence(n):
    values = []
    while n > 1:

        values.append(int(n))

        if n % 2 == 0:
            n = n / 2

        elif n % 2 == 1:
            n = 3 * n + 1

        else:
            n *= 3 * n + 1

    values.append(1)

    return values


class MyMainWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        title = "Anthony Mudet" + datetime.now().strftime(" à  %H:%M:%S")
        self.setWindowTitle(title)

        self.le = QLineEdit()
        self.te = QPlainTextEdit()

        self.lb = QLabel()
        self.lb.setFixedWidth(self.width())
        self.lb.setFixedHeight(self.height())
        self.lb.setFrameShape(QFrame.Panel)

        self.px = QPixmap(self.lb.width(), self.lb.height())

        label = QLabel("Saisir un nombre et cliquer")
        self.bu = QPushButton("Calcul ...")

        self.bu.clicked.connect(self.DisplayMessage)

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.bu)
        layout.addWidget(self.te)
        layout.addWidget(self.lb)
        self.setLayout(layout)

    def DisplayMessage(self):
        values = GenerateSyracusSequence(int(self.le.text()))

        self.te.clear()

        for val in values:
            self.te.insertPlainText(str(val) + "\n")

        self.te.insertPlainText("nombre de termes dans la suite :" + str(len(values)) + "\n")
        self.te.insertPlainText("valeur max de la suite :" + str(max(values)) + "\n")

        self.Draw(values)

    def Draw(self, values):

        self.px.fill(QColor(200,200,200))
        painter = QPainter(self.px)
        painter.setPen(QColor(255, 0, 0))

        for i in range(len(values)):

            x1 = i * self.lb.width() // len(values)
            y1 = values[i] * self.lb.height() // max(values)

            x2 = (i + 1) * self.lb.width() // len(values)
            y2 = values[i + 1] * self.lb.height() // max(values) if i + 1 < len(values) else y1

            painter.drawLine(x1, self.lb.height() - y1, x2, self.lb.height() - y2)

        self.lb.setPixmap(self.px)

    def closeEvent(self, a0):

        self.mb = QMessageBox().question(None, "Fermer", "Voulez-vous fermer la fenêtre ?", QMessageBox.Yes | QMessageBox.No)

        if self.mb == QMessageBox.Yes:
            a0.accept()

        else:
            a0.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()

    # lancement de la gestion des evenements
    app.exec_()
