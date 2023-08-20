# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Admin\Downloads\data\HoSoBenhAn\res\ui\Manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1006, 465)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.managemenBox = QtWidgets.QFrame(Form)
        self.managemenBox.setStyleSheet("#managemenBox .QTabBar::tab,\n"
"#Device .QTabBar::tab,\n"
"#managemenTab .QTabBar::tab {\n"
"    color: rgb(3, 14, 22);\n"
"    padding: 10px;\n"
"    font: 87 10pt \"Segoe UI Black\";\n"
"    width:100px;\n"
"    height:20px;\n"
"    background-color:white;\n"
"    margin-left: 5px;\n"
"    margin-right:5px;\n"
"    border-radius: 20px;\n"
"margin-top:10px;\n"
"}\n"
"#managemenBox .QTabBar::tab:selected,\n"
"#Device .QTabBar::tab:selected,\n"
"#managemenTab .QTabBar::tab:selected {\n"
"    background-color: rgb(3, 14,22);\n"
"    color: white;\n"
"    font: 87 11pt \"Segoe UI Black\";\n"
"    width:100px;\n"
" }\n"
"#managemenBox .QTabWidget::pane,\n"
"#Device .QTabWidget::pane,\n"
"#managemenTab .QTabWidget::pane{\n"
"     border: 0;\n"
"}\n"
"#managemenBox .QWidget,\n"
"#Device .QWidget,\n"
"#managemenTab .QWidget {\n"
"     background-color: transparent;\n"
"}\n"
"#managemenBox .QTabWidget::tab-bar,\n"
"#Device .QTabWidget::tab-bar,\n"
"#managemenTab .QTabWidget::tab-bar {\n"
"     alignment: center;\n"
"}")
        self.managemenBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.managemenBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.managemenBox.setObjectName("managemenBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.managemenBox)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.managemenTab = QtWidgets.QTabWidget(self.managemenBox)
        self.managemenTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.managemenTab.setStyleSheet("")
        self.managemenTab.setObjectName("managemenTab")
        self.semiBoardingPage_2 = QtWidgets.QWidget()
        self.semiBoardingPage_2.setObjectName("semiBoardingPage_2")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.semiBoardingPage_2)
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.containersemiBoardingPage = QtWidgets.QFrame(self.semiBoardingPage_2)
        self.containersemiBoardingPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.containersemiBoardingPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.containersemiBoardingPage.setObjectName("containersemiBoardingPage")
        self.gridLayout_37.addWidget(self.containersemiBoardingPage, 0, 0, 1, 1)
        self.managemenTab.addTab(self.semiBoardingPage_2, "")
        self.BoardingPage = QtWidgets.QWidget()
        self.BoardingPage.setObjectName("BoardingPage")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.BoardingPage)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.containerBoardingPage = QtWidgets.QFrame(self.BoardingPage)
        self.containerBoardingPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.containerBoardingPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.containerBoardingPage.setObjectName("containerBoardingPage")
        self.gridLayout_39.addWidget(self.containerBoardingPage, 0, 0, 1, 1)
        self.managemenTab.addTab(self.BoardingPage, "")
        self.gridLayout_2.addWidget(self.managemenTab, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.managemenBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.managemenTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.managemenTab.setTabText(self.managemenTab.indexOf(self.semiBoardingPage_2), _translate("Form", "Nội trú"))
        self.managemenTab.setTabText(self.managemenTab.indexOf(self.BoardingPage), _translate("Form", "Bán trú"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())