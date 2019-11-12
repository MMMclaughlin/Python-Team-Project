import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import random
import webbrowser

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Newcastle University Services Shortcuts'
        self.left = 500
        self.top = 500
        self.width = 1000
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('hero-locations.jpg'))
        self.label.setGeometry(0,0,1000,500)

        def open_webbrowser():
            webbrowser.open('http://www.google.com')

        button1 = QPushButton('BLACKBOARD', self)
        button1.setToolTip('Lecture ReCaps and learning materials')
        button1.setGeometry(120, 80, 120, 60)
        button1.clicked.connect(webbrowser.open)

        button2 = QPushButton('NUCODE', self)
        button2.setToolTip('GitHub for students (GitLab)')
        button2.setGeometry(120, 160, 120, 60)
        #button2.clicked.connect(self.on_click2)

        button3 = QPushButton('NESS', self)
        button3.setToolTip('Place for submitting your coursework')
        button3.setGeometry(120, 240, 120, 60)
        #button3.clicked.connect(self.on_click3)

        button4 = QPushButton('RAS', self)
        button4.setToolTip('Remote Application Service')
        button4.setGeometry(120, 320, 120, 60)
        #button4.clicked.connect(self.on_click4)

        button5 = QPushButton('PORTFOLIO', self)
        button5.setToolTip('Your student portfolio')
        button5.setGeometry(120, 400, 120, 60)
        #button5.clicked.connect(self.on_click5)

        self.show()

    @pyqtSlot()
    def on_click1(self):
        print('ok')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())