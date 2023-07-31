import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
import bcrypt

from src.activity.LoginActivity import LoginActivity
from src.model.User import User
from src.service.Connection import Connection
from src.service.UserService import UserService


class Start():
    def startLayout(self):
        if not os.path.exists('assets'):
            os.makedirs('assets')
        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon('res/drawable/icons/icon.png'))
        Connection.getInstance()
        self.userService = UserService()
        listUser = self.userService.getAll(User)
        if len(listUser) <= 0:
            password = "admin"
            passwordHash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            user = User(UserName="admin", Password=passwordHash.decode('utf-8'))
            self.userService.create(user)

        self.window = LoginActivity()
        self.window.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    Start().startLayout()
