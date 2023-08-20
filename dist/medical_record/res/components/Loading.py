
from PyQt5 import QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel, QDesktopWidget


class LoadingWidget(QFrame):
    def __init__(self, parent=None):
        super(LoadingWidget, self).__init__(parent)
        self.parent = QDesktopWidget().screenGeometry()

    def startLoading(self):
        # get width and height of centralwidget
        width = self.parent.width()
        height = self.parent.height()
        self.setGeometry(0, 0, width, height+100)
        self.setStyleSheet("background-color: rgba(0, 0, 0,0.5);")

        # set movie center
        self.labelMovie = QLabel(self)
        self.labelMovie.setGeometry(QtCore.QRect(width / 2 - 80, height / 2 - 80, 100, 100))
        self.labelMovie.setStyleSheet("background-color: transparent;")
        self.movie = QMovie("res/drawable/icons/loading.gif")
        self.labelMovie.setMovie(self.movie)
        self.movie.setScaledSize(QtCore.QSize(100, 100))
        self.movie.start()

        self.lbTitle = QLabel(self)
        self.lbTitle.setGeometry(QtCore.QRect(width / 2 - 100, height / 2 + 100, 200, 50))
        self.lbTitle.setStyleSheet("background-color: transparent; color: white; font-size: 20px;")
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(500)
        self.count = 0

        self.show()
    def stopTopLoading(self):
        self.hide()

    def handleTimer(self):
        if self.count == 0:
            self.lbTitle.setText("Loading.")
        elif self.count == 1:
            self.lbTitle.setText("Loading..")
        elif self.count == 2:

           self.lbTitle.setText("Loading...")
        elif self.count == 3:
            self.lbTitle.setText("Loading....")
            self.count = -1
        self.count += 1


