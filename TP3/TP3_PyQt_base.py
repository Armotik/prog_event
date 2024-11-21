import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QStatusBar, QFileDialog, QColorDialog
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from datetime import datetime
import random
import pickle

class myHisto:
    """Classe myHisto pour stocker l'histogramme"""

    def __init__(self):
        print('Méthode __init__()  de la classe myHisto')
        self.m_list = [0] * 10  # 10 bins par défaut
        self.m_size = 10        # Taille fixe de l'histogramme
        self.m_max = 99        # Valeur maximale des bins
        self.color = QColor(Qt.blue)  # Couleur des barres

    def set_random_values(self):
        self.m_list = [random.randint(0, self.m_max) for _ in range(self.m_size)]

    def total(self):
        return sum(self.m_list)

class MyMainWindow(QMainWindow):
    """ Classe de l'application principale"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # Attributs de la fenêtre principale
        self.setGeometry(300, 300, 600, 450)
        self.titleInfo = "VOTRE_NOM"
        self.titleMainWindow = self.titleInfo + datetime.now().strftime("  %H:%M:%S") + ' | Res: ' + str(self.width()) + 'x' + str(self.height())
        self.setWindowTitle(self.titleMainWindow)

        # Barre de status pour afficher les infos
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Zone d'informations, peut toujours servir")

        # Création d'une instance de la classe myHisto
        self.mHisto = myHisto()

        self.createActions()
        self.createMenus()

    def resizeEvent(self, event):
        self.titleMainWindow = self.titleInfo + datetime.now().strftime("  %H:%M:%S") + '| Res: ' + str(self.width()) + 'x' + str(self.height())
        self.setWindowTitle(self.titleMainWindow)

    def createActions(self):
        """ Créer ici les actions d'item de menu ainsi que connexions signal/slot, à compléter"""
        self.exitAct = QAction(" &Quit", self)
        self.exitAct.setShortcut("Ctrl+X")
        self.exitAct.triggered.connect(self.myExit)

        self.openAct = QAction("&Open", self)
        self.openAct.setShortcut("Ctrl+O")
        self.openAct.triggered.connect(self.openFile)

        self.saveAct = QAction("&Save", self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.triggered.connect(self.saveFile)

        self.restoreAct = QAction("&Restore", self)
        self.restoreAct.triggered.connect(self.restoreFile)

        self.clearAct = QAction("&Clear", self)
        self.clearAct.triggered.connect(self.clearHistogram)

        self.colorAct = QAction("&Color", self)
        self.colorAct.triggered.connect(self.changeColor)

    def createMenus(self):
        """ Créer ici les menu et les items de menu"""
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self.openAct)
        fileMenu.addAction(self.saveAct)
        fileMenu.addAction(self.restoreAct)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAct)

        displayMenu = self.menuBar().addMenu("&Display")
        displayMenu.addAction(self.clearAct)
        displayMenu.addAction(self.colorAct)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawHistogram(qp)
        qp.end()

    def drawHistogram(self, qp):
        qp.setBrush(self.mHisto.color)
        qp.setPen(Qt.black)

        bar_width = self.width() // len(self.mHisto.m_list)
        for i, value in enumerate(self.mHisto.m_list):
            bar_height = int((value / self.mHisto.m_max) * self.height())
            qp.drawRect(i * bar_width, self.height() - bar_height, bar_width - 2, bar_height)

    def openFile(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Histogram File", "", "Data Files (*.dat)", options=options)

        if file_name:
            try:
                with open(file_name, 'r') as file:
                    self.mHisto.m_list = [int(line.strip()) for line in file.readlines()]
                self.statusBar.showMessage("Histogram opened!")
                self.update()
            except Exception as e:
                self.statusBar.showMessage(f"Error: {e}")

    def saveFile(self):
        try:
            with open("saveHisto.bin", "wb") as file:
                pickle.dump(self.mHisto.m_list, file)
            self.statusBar.showMessage("Histogram saved!")
        except Exception as e:
            self.statusBar.showMessage(f"Error: {e}")

    def restoreFile(self):
        try:
            with open("saveHisto.bin", "rb") as file:
                self.mHisto.m_list = pickle.load(file)
            self.statusBar.showMessage("Histogram restored!")
            self.update()
        except Exception as e:
            self.statusBar.showMessage(f"Error: {e}")

    def clearHistogram(self):
        self.mHisto.m_list = [0] * self.mHisto.m_size
        self.statusBar.showMessage("Histogram cleared!")
        self.update()

    def changeColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.mHisto.color = color
            self.statusBar.showMessage("Color changed!")
            self.update()

    def myExit(self):
        """ Slot associé à exitAct, instance de QAction"""
        self.statusBar.showMessage("Quit ...")
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()