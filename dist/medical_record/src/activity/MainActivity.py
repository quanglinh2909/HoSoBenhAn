
from PyQt5.QtWidgets import QMainWindow
from res.components.pyqt_toast.toast import Toast
from res.layout.MainLayout import Ui_MainWindow
from src.widget.ConfigWiget import ConfigWiget
from src.widget.ManagerWiget import ManagerWiget


class MainWindowActivity(QMainWindow, Ui_MainWindow):
    def __init__(self,userName=None):
        super(MainWindowActivity, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Cơ sở BTXH. Ân Phúc")
        self.pageCurrent = None
        self.toast = Toast(text="", duration=2, parent=self)

        self.managerWiget = ManagerWiget(context=self.containerManager, parent=self)
        self.configWiget = ConfigWiget(context=self.containeConfig, parent=self)

        self.showManagePage()

        self.handleEvent()

    def handleEvent(self):
        self.btnManager.clicked.connect(self.showManagePage)
        self.btnConfig.clicked.connect(self.showConfigPage)




    def showManagePage(self):
        if self.pageCurrent != self.managerPage:
            self.stackedWidgetHome.setCurrentWidget(self.managerPage)
            # btnParkingClick(self.ParkingLeftBtn_2)
            self.pageCurrent = self.managerPage

    def showConfigPage(self):
        if self.pageCurrent != self.configPage:
            self.stackedWidgetHome.setCurrentWidget(self.configPage)
            # btnParkingClick(self.ParkingLeftBtn_2)
            self.pageCurrent = self.configPage
