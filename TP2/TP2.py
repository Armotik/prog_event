from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt, QRect, QSize, pyqtSignal, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class MyBrowserWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(800, 600)
        self.myBrowserWidget = QWebEngineView(self)
        self.myBrowserWidget.setGeometry(0, 0, 800, 600)
        self.url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name'
        self.myBrowserWidget.load(QUrl(self.url))

    def changeLetter(self, letter):
        new_url = self.url + f'#{letter}'
        self.myBrowserWidget.load(QUrl(new_url))

class MyMainWindow(QWidget):
    sendLetter = pyqtSignal(str)  # Signal pour envoyer une lettre

    def __init__(self, parent=None):
        super().__init__(parent)

        # Attributs de la fenêtre principale
        self.setGeometry(300, 300, 800, 400)
        self.setMinimumSize(QSize(400, 200))
        self.setWindowTitle('My Main Window')
        self.paint_counter = 0  # Compteur d'événements Paint
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.grid_columns = 13
        self.grid_rows = 2
        self.cell_width = self.width() // self.grid_columns
        self.cell_height = self.height() // self.grid_rows
        self.browser_window = MyBrowserWindow()

        self.sendLetter.connect(self.browser_window.changeLetter)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.browser_window)

    def paintEvent(self, event):
        # Incrémentation du compteur d'événements Paint
        self.paint_counter += 1
        print(f"Paint event N° {self.paint_counter}")

        # Dessin
        qp = QPainter()
        qp.begin(self)

        # Tracé de la grille et des lettres
        self.cell_width = self.width() // self.grid_columns
        self.cell_height = self.height() // self.grid_rows

        for row in range(self.grid_rows):
            for col in range(self.grid_columns):
                index = row * self.grid_columns + col
                if index < len(self.alphabet):
                    rect = QRect(col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height)
                    qp.drawRect(rect)
                    qp.drawText(rect, Qt.AlignCenter, self.alphabet[index])

        qp.end()

    def mouseReleaseEvent(self, event):
        # Récupération de la position du clic
        x = event.x()
        y = event.y()

        col = x // self.cell_width
        row = y // self.cell_height
        index = row * self.grid_columns + col

        if 0 <= index < len(self.alphabet):
            letter = self.alphabet[index]
            print(f"Mouse click at: ({x}, {y}) in cell ({row}, {col}), letter: {letter}")
            self.sendLetter.emit(letter)
        else:
            print(f"Mouse click at: ({x}, {y}) outside the grid")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.update()
        elif event.key() == Qt.Key_E:
            self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    main_window.browser_window.show()
    sys.exit(app.exec_())
