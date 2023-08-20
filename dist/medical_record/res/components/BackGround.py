
from PyQt5 import QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QMainWindow, QFrame, QLabel

class BackgroundWidget(QFrame):
    def __init__(self, parent=None):
        super(BackgroundWidget, self).__init__(parent)
        self.parent = parent

    def showBackGround(self):
        # get width and height of centralwidget
        width = self.parent.centralwidget.width()
        height = self.parent.centralwidget.height()
        self.setGeometry(0, 0, width, height+100)
        self.setStyleSheet("background-color: rgba(0, 0, 0,0.5);")
        self.show()
    def hideBackGround(self):
        self.hide()




