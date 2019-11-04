def test():
    print("this is working spec 4")

# TEST TEST TEST

# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot
#
#
# class App(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'Practical 3, Newcastle University'
#         self.left = 1080
#         self.top = 650
#         self.width = 800
#         self.height = 400
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('File')
#         editMenu = mainMenu.addMenu('Edit')
#         viewMenu = mainMenu.addMenu('View')
#         searchMenu = mainMenu.addMenu('Search')
#         toolsMenu = mainMenu.addMenu('Tools')
#         helpMenu = mainMenu.addMenu('Help')
#
#         exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
#         exitButton.setShortcut('Ctrl+Q')
#         exitButton.setStatusTip('Exit application')
#         exitButton.triggered.connect(self.close)
#         fileMenu.addAction(exitButton)
#
#         undoButton = QAction(QIcon('exit24.png'), 'Undo', self)
#         undoButton.setShortcut('Ctrl+M')
#         undoButton.setStatusTip('Exit Z application')
#         undoButton.triggered.connect(self.close)
#         editMenu.addAction(undoButton)
#
#         graduationButton = QAction(QIcon('exit24.png'), 'GRADUATION', self)
#         graduationButton.setShortcut('Ctrl+G')
#         graduationButton.setStatusTip('GRADUATE!')
#         graduationButton.triggered.connect(self.close)
#         helpMenu.addAction(graduationButton)
#
#         # Create textbox
#         self.textbox = QLineEdit(self)
#         self.textbox.move(20, 20)
#         self.textbox.resize(280, 40)
#
#         # Create a button in the window
#         self.button = QPushButton('Show text', self)
#         self.button.move(20, 80)
#
#         # connect button to function on_click
#         self.button.clicked.connect(self.on_click)
#         self.show()
#
#
#
#     @pyqtSlot()
#     def on_click(self):
#         textboxValue = self.textbox.text()
#         QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
#                              QMessageBox.Ok)
#         self.textbox.setText("")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt paint - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

        self.show()

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)

        qp.setPen(Qt.black)
        size = self.size()

        for i in range(1024):
            x = random.randint(1, size.width()-2)
            y = random.randint(1, size.height()-2)
            qp.drawPoint(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
