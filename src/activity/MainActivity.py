
from PyQt5.QtWidgets import QMainWindow
from res.components.pyqt_toast.toast import Toast
from res.layout.MainLayout import Ui_MainWindow
from src.widget.ManagerWiget import ManagerWiget


class MainWindowActivity(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowActivity, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Quản lý bệnh nhân")
        self.pageCurrent = None

        self.ManagerWiget = ManagerWiget(context=self.containerManager, parent=self)
        self.toast = Toast(text="", duration=2, parent=self)

        self.showManagePage()


    def showManagePage(self):
        if self.pageCurrent != self.managerPage:
            self.stackedWidgetHome.setCurrentWidget(self.managerPage)
            # btnParkingClick(self.ParkingLeftBtn_2)
            self.pageCurrent = self.managerPage
