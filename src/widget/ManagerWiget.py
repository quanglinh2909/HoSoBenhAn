from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QLabel

from res.layout.ManagerLayout import Ui_Form

from src.widget.MemberWiget import MemberWiget

class ManagerWiget(QMainWindow, Ui_Form):
    def __init__(self, parent=None, context=None):
        super(ManagerWiget, self).__init__(context)
        self.setupUi(context)
        self.parent = parent

        self.memberWiget = MemberWiget(context=self.containersemiBoardingPage, parent=self)
        self.managemenTab.setCurrentIndex(0)
