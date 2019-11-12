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
        self.title = 'Shortcuts for Newcastle University CS Services'
        self.left = 500
        self.top = 500
        self.width = 1000
        self.height = 500
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('NUicon.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('BackGround2.jpg'))
        self.label.setGeometry(0,0,1000,500)

        def open_webbrowser1():
            webbrowser.open('http://blackboard.ncl.ac.uk/')

        button1 = QPushButton('BLACKBOARD', self)
        button1.setToolTip('Lecture ReCaps and learning materials')
        button1.setGeometry(60, 60, 150, 60)
        button1.clicked.connect(open_webbrowser1)

        def open_webbrowser2():
            webbrowser.open('https://nucode.ncl.ac.uk/users/sign_in')

        button2 = QPushButton('NUCODE', self)
        button2.setToolTip('GitHub for students (GitLab)')
        button2.setGeometry(60, 140, 150, 60)
        button2.clicked.connect(open_webbrowser2)

        def open_webbrowser3():
            webbrowser.open('https://ness.ncl.ac.uk')

        button3 = QPushButton('NESS', self)
        button3.setToolTip('Place for submitting your coursework')
        button3.setGeometry(60, 220, 150, 60)
        button3.clicked.connect(open_webbrowser3)

        def open_webbrowser4():
            webbrowser.open('https://ras.ncl.ac.uk')

        button4 = QPushButton('RAS', self)
        button4.setToolTip('Remote Application Service')
        button4.setGeometry(60, 300, 150, 60)
        button4.clicked.connect(open_webbrowser4)

        def open_webbrowser5():
            webbrowser.open('https://portfolio.ncl.ac.uk/accounts/login/')

        button5 = QPushButton('PORTFOLIO', self)
        button5.setToolTip('Your student portfolio')
        button5.setGeometry(60, 380, 150, 60)
        button5.clicked.connect(open_webbrowser5)

        def open_webbrowser6():
            webbrowser.open('https://gateway.ncl.ac.uk/idp/profile/SAML2/Redirect/SSO?execution=e8s1')

        button6 = QPushButton('LIBRARY', self)
        button6.setToolTip('University library portal')
        button6.setGeometry(230, 60, 150, 60)
        button6.clicked.connect(open_webbrowser6)

        def open_webbrowser7():
            webbrowser.open('')

        button7 = QPushButton('', self)
        button7.setToolTip('')
        button7.setGeometry(230, 140, 150, 60)
        button7.clicked.connect(open_webbrowser7)

        def open_webbrowser8():
            webbrowser.open('')

        button8 = QPushButton('', self)
        button8.setToolTip('')
        button8.setGeometry(230, 220, 150, 60)
        button8.clicked.connect(open_webbrowser8)

        def open_webbrowser9():
            webbrowser.open('')

        button9 = QPushButton('', self)
        button9.setToolTip('')
        button9.setGeometry(230, 300, 150, 60)
        button9.clicked.connect(open_webbrowser9)

        def open_webbrowser10():
            webbrowser.open('')

        button10 = QPushButton('', self)
        button10.setToolTip('')
        button10.setGeometry(230, 380, 150, 60)
        button10.clicked.connect(open_webbrowser10)

        self.show()

    @pyqtSlot()
    def on_click1(self):
        print('ok')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
