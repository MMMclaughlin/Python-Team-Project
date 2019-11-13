import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QDialog
from PyQt5.QtGui import QPainter, QColor, QPen, QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import *
import webbrowser

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(1000,500)
        self.center()
        self.setWindowTitle('Shortcuts of useful services for Computer Science students')
        self.setWindowIcon(QIcon('NUicon.png'))

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
            webbrowser.open('https://portfolio.ncl.ac.uk/accounts/login/')

        button2 = QPushButton('PORTFOLIO', self)
        button2.setToolTip('Your student\'s portfolio')
        button2.setGeometry(60, 140, 150, 60)
        button2.clicked.connect(open_webbrowser2)

        def open_webbrowser3():
            webbrowser.open('https://nucode.ncl.ac.uk/users/sign_in')

        button3 = QPushButton('NUCODE', self)
        button3.setToolTip('GitHub for students (GitLab)')
        button3.setGeometry(60, 220, 150, 60)
        button3.clicked.connect(open_webbrowser3)

        def open_webbrowser4():
            webbrowser.open('https://ness.ncl.ac.uk')

        button4 = QPushButton('NESS', self)
        button4.setToolTip('Place for submitting your coursework')
        button4.setGeometry(60, 300, 150, 60)
        button4.clicked.connect(open_webbrowser4)

        def open_webbrowser5():
            webbrowser.open('https://ras.ncl.ac.uk')

        button5 = QPushButton('RAS', self)
        button5.setToolTip('Remote Application Service')
        button5.setGeometry(60, 380, 150, 60)
        button5.clicked.connect(open_webbrowser5)

        def open_webbrowser6():
            webbrowser.open('') # UPDATE LIB LINK!

        button6 = QPushButton('LIBRARY', self)
        button6.setToolTip('University Library')
        button6.setGeometry(230, 60, 150, 60)
        button6.clicked.connect(open_webbrowser6)

        def open_webbrowser7():
            webbrowser.open('https://office365.ncl.ac.uk')

        button7 = QPushButton('EMAIL', self)
        button7.setToolTip('Your university\'s OutLook email')
        button7.setGeometry(230, 140, 150, 60)
        button7.clicked.connect(open_webbrowser7)

        def open_webbrowser8():
            webbrowser.open('https://s3p.ncl.ac.uk/Login/Index.aspx')

        button8 = QPushButton('S3P', self)
        button8.setToolTip('Newcastle University\'s Student Self Service Portal')
        button8.setGeometry(230, 220, 150, 60)
        button8.clicked.connect(open_webbrowser8)

        def open_webbrowser9():
            webbrowser.open('https://appspay.ncl.ac.uk/sport/Login')

        button9 = QPushButton('SPORT', self)
        button9.setToolTip('Get a membership for using sport facilities')
        button9.setGeometry(230, 300, 150, 60)
        button9.clicked.connect(open_webbrowser9)

        def open_webbrowser10():
            webbrowser.open('')

        button10 = QPushButton('', self)
        button10.setToolTip('')
        button10.setGeometry(230, 380, 150, 60)
        button10.clicked.connect(open_webbrowser10)

        self.show()

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def on_click1(self):
        print('ok')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    splash_pix = QPixmap('BackGround1.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.SplashScreen)
    splash.setEnabled(False)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    time.sleep(2)

    ex = App()
    splash.finish(ex)
    sys.exit(app.exec_())