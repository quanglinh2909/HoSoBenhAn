# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/link/Documents/Python/HoSoBenhAn/res/ui/Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 695)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("#frameBox{\n"
"border-image: url(:/images/res/drawable/icons/anh-background-y-te_034616052.jpg) stretch stretch;\n"
"background-color:black;\n"
"\n"
"\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frameBox = QtWidgets.QFrame(self.centralwidget)
        self.frameBox.setStyleSheet("QFrame#frameBox{\n"
"background-color: rgb(240, 240, 240);\n"
"border: 1px solid rgb(202, 202, 202);\n"
"border-radius: 10px;\n"
"\n"
"};\n"
"\n"
"")
        self.frameBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBox.setObjectName("frameBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameBox)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frameBox)
        self.stackedWidget.setStyleSheet("QFrame{\n"
"border:none;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageLogin = QtWidgets.QWidget()
        self.pageLogin.setStyleSheet("")
        self.pageLogin.setObjectName("pageLogin")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageLogin)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.pageLogin)
        self.frame_4.setMinimumSize(QtCore.QSize(349, 506))
        self.frame_4.setMaximumSize(QtCore.QSize(349, 600))
        self.frame_4.setStyleSheet("QFrame#frame_4 {background-color: white;\n"
"border-radius: 10px;}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label.setStyleSheet("QLabel#label {\n"
"color: #55595D;\n"
"font: 24pt \"Open Sans Condensed\";\n"
"font-weight:600;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(49, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_44 = QtWidgets.QLabel(self.frame_4)
        self.label_44.setStyleSheet("QLabel {color: rgb(0, 0, 0);\n"
"font: 10pt \"Open Sans\";}")
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_4.addWidget(self.label_44)
        self.UserNameTxt = QtWidgets.QLineEdit(self.frame_4)
        self.UserNameTxt.setMinimumSize(QtCore.QSize(300, 40))
        self.UserNameTxt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.UserNameTxt.setFont(font)
        self.UserNameTxt.setStyleSheet("QLineEdit {\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    font: 11pt \"Open Sans\";\n"
"    margin-left: 5px;\n"
"    margin-right: 5px;\n"
"    border: 1px solid rgb(220, 220, 220);\n"
"}\n"
"")
        self.UserNameTxt.setText("")
        self.UserNameTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.UserNameTxt.setObjectName("UserNameTxt")
        self.verticalLayout_4.addWidget(self.UserNameTxt)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_43 = QtWidgets.QLabel(self.frame_4)
        self.label_43.setStyleSheet("QLabel {color: rgb(0, 0, 0);\n"
"font: 10pt \"Open Sans\";}")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_2.addWidget(self.label_43)
        self.PasswordTxt = QtWidgets.QLineEdit(self.frame_4)
        self.PasswordTxt.setMinimumSize(QtCore.QSize(300, 40))
        self.PasswordTxt.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.PasswordTxt.setFont(font)
        self.PasswordTxt.setStyleSheet("QLineEdit {\n"
"    color: black;\n"
"    background-color: white;\n"
"    border-radius: 10px;\n"
"    font: 11pt \"Open Sans\";\n"
"    margin-left: 5px;\n"
"    margin-right: 5px;\n"
"    border: 1px solid rgb(220, 220, 220);\n"
"}\n"
"")
        self.PasswordTxt.setText("")
        self.PasswordTxt.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordTxt.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordTxt.setObjectName("PasswordTxt")
        self.verticalLayout_2.addWidget(self.PasswordTxt)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.frame_9 = QtWidgets.QFrame(self.frame_4)
        self.frame_9.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_9.setStyleSheet("background-color: white;\n"
"border:none;")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.LoginBtn = QtWidgets.QPushButton(self.frame_10)
        self.LoginBtn.setMinimumSize(QtCore.QSize(100, 30))
        self.LoginBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LoginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LoginBtn.setStyleSheet("background-color: #55595D;\n"
"color: white;\n"
"border-radius:5px;\n"
"font: 11pt \"Open Sans\";")
        self.LoginBtn.setObjectName("LoginBtn")
        self.horizontalLayout_4.addWidget(self.LoginBtn)
        self.horizontalLayout_5.addWidget(self.frame_10)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget_2.addWidget(self.page_2)
        self.verticalLayout_3.addWidget(self.stackedWidget_2)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.pageLogin)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 58))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 34, 0, 0)
        self.horizontalLayout_6.setSpacing(13)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setMaximumSize(QtCore.QSize(40, 60))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/icon/res/drawable/icons/Frame_185.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMaximumSize(QtCore.QSize(40, 60))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/icon/res/drawable/icons/Frame_186.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setMaximumSize(QtCore.QSize(40, 60))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/icon/res/drawable/icons/Frame_187.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout_5.addWidget(self.frame_6)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.pageLogin)
        self.verticalLayout.addWidget(self.stackedWidget, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frameBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Đăng nhập"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Tài khoản</span></p></body></html>"))
        self.UserNameTxt.setPlaceholderText(_translate("MainWindow", "Nhập số điện thoại"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Mật khẩu</span></p></body></html>"))
        self.PasswordTxt.setPlaceholderText(_translate("MainWindow", "Nhập mật khẩu"))
        self.LoginBtn.setText(_translate("MainWindow", "Đăng nhập"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
