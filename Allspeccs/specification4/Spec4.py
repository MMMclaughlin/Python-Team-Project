import sys
import time
import webbrowser
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

# Creating main window class

class App(QMainWindow):

    # User interface function

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Main window, geometry, title, icon

        self.resize(1000,500)
        self.center()
        self.setWindowTitle('Shortcuts of useful services for Computer Science students')
        self.setWindowIcon(QIcon('images/NUicon.png'))

        # Adding background image for main winwod

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('images/BackGround2.jpg'))
        self.label.setGeometry(0,0,1000,500)

        # Defining functions (opening webbrowser and links) for each button
        # Creating buttons with title, tooltips, geometry and connecting to functions

        def open_webbrowser1():
            webbrowser.open('http://blackboard.ncl.ac.uk/')

        button1 = QPushButton('BLACKBOARD', self)
        button1.setToolTip('Lecture ReCaps and learning materials')
        button1.setGeometry(60, 60, 170, 60)
        button1.clicked.connect(open_webbrowser1)

        def open_webbrowser2():
            webbrowser.open('https://portfolio.ncl.ac.uk/accounts/login/')

        button2 = QPushButton('PORTFOLIO', self)
        button2.setToolTip('Your student\'s portfolio')
        button2.setGeometry(60, 140, 170, 60)
        button2.clicked.connect(open_webbrowser2)

        def open_webbrowser3():
            webbrowser.open('https://nucode.ncl.ac.uk/users/sign_in')

        button3 = QPushButton('NUCODE', self)
        button3.setToolTip('GitHub for students (GitLab)')
        button3.setGeometry(60, 220, 170, 60)
        button3.clicked.connect(open_webbrowser3)

        def open_webbrowser4():
            webbrowser.open('https://ness.ncl.ac.uk')

        button4 = QPushButton('NESS', self)
        button4.setToolTip('Place for submitting your coursework')
        button4.setGeometry(60, 300, 170, 60)
        button4.clicked.connect(open_webbrowser4)

        def open_webbrowser5():
            webbrowser.open('https://ras.ncl.ac.uk')

        button5 = QPushButton('RAS', self)
        button5.setToolTip('Remote Application Service')
        button5.setGeometry(60, 380, 170, 60)
        button5.clicked.connect(open_webbrowser5)

        def open_webbrowser6():
            webbrowser.open('') # UPDATE LIB LINK!

        button6 = QPushButton('LIBRARY', self)
        button6.setToolTip('University Library')
        button6.setGeometry(250, 60, 170, 60)
        button6.clicked.connect(open_webbrowser6)

        def open_webbrowser7():
            webbrowser.open('https://appspay.ncl.ac.uk/sport/Login')

        button7 = QPushButton('SPORT', self)
        button7.setToolTip('Get a membership to start using sport facilities')
        button7.setGeometry(250, 140, 170, 60)
        button7.clicked.connect(open_webbrowser7)

        def open_webbrowser8():
            webbrowser.open('https://office365.ncl.ac.uk')

        button8 = QPushButton('EMAIL', self)
        button8.setToolTip('Your university\'s OutLook email')
        button8.setGeometry(250, 220, 170, 60)
        button8.clicked.connect(open_webbrowser8)

        def open_webbrowser9():
            webbrowser.open('https://s3p.ncl.ac.uk/Login/Index.aspx')

        button9 = QPushButton('S3P', self)
        button9.setToolTip('Newcastle University\'s Student Self Service Portal')
        button9.setGeometry(250, 300, 170, 60)
        button9.clicked.connect(open_webbrowser9)

        def on_button_clicked():
            alert = QMessageBox()
            alert.setText('\nPressing button with the name of the service will open a webbrowser '
                          '(or a new tab, if webbrowser is already opened) with a login page. \n\n'
                          'Place your cursor over the button to see more information. \n\n'
                          'Created by Tom Sevcov for CSC1034 Team Project using Python and PyQT5 library.')
            alert.exec_()

        button10 = QPushButton('INFO!', self)
        button10.setToolTip('Press to know more about the app and functionality')
        button10.setGeometry(250, 380, 170, 60)
        button10.setStyleSheet("background-color: red")
        button10.clicked.connect(on_button_clicked)

        # Creating another button (NUSU) with background image (label)

        def open_webbrowser11():
            webbrowser.open('https://www.nusu.co.uk')

        button11 = QPushButton('NUSU', self)
        button11.setToolTip('Newcastle Universrity Student Union')
        button11.setGeometry(615, 380, 150, 60)
        button11.setStyleSheet("background-color: white")
        button11.label = QLabel(button11)
        button11.label.setPixmap(QPixmap('images/NUSUbutton.jpg'))
        button11.label.setGeometry(3, 3, 144, 54)
        button11.clicked.connect(open_webbrowser11)

        # Showing window with buttons

        self.show()

    # Defining a function that always opens app (main window) in the center of screen

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

# Running the app

if __name__ == '__main__':

    app = QApplication(sys.argv)

    # Changing the style of the app (appearance)

    app.setStyle('Fusion')

    # Creating splash screen

    splash_pix = QPixmap('images/BackGround1.jpg')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.SplashScreen)
    splash.setEnabled(False)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()

    # Setting the time to show splash screen to 2 seconds

    time.sleep(2)

    ex = App()
    splash.finish(ex)
    sys.exit(app.exec_())