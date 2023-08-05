import os

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from res.components.Loading import LoadingWidget
from res.components.pyqt_toast.toast import Toast
from res.layout.LoginLayout import Ui_MainWindow
from src.activity.MainActivity import MainWindowActivity
from src.service.UserService import UserService


class LoginActivity(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(LoginActivity, self).__init__()
        self.setupUi(self)
        self.showMaximized()
        self.setWindowTitle("Quản lý bệnh nhân")
        self.userService = UserService()

        self.UserNameTxt.setFocus()

        self.LoginBtn.clicked.connect(self.login)
        self.toast = Toast(text="", duration=2, parent=self)

        self.UserNameTxt.setText("admin")
        self.PasswordTxt.setText("admin")

    def login(self):
        phone = self.UserNameTxt.text().strip()
        password = self.PasswordTxt.text().strip()
        if phone == '':
            self.UserNameTxt.setFocus()
            self.toast.showToast("Vui lòng nhập số điện thoại", type=Toast.ERROR)
            return
        if password == '':
            self.PasswordTxt.setFocus()
            self.toast.showToast("Vui lòng nhập mật khẩu", type=Toast.ERROR)
            return
        self.loading = LoadingWidget(self)
        self.loading.startLoading()
        res = self.userService.login(phone, password)
        self.loading.stopTopLoading()
        if res is None or res is False:
            self.toast.showToast("Đăng nhập thất bại", type=Toast.ERROR)
            return

        self.mainWindowActivity = MainWindowActivity(userName=phone)
        self.mainWindowActivity.show()
        self.close()
