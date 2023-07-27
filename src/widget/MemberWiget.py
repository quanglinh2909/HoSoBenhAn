from datetime import datetime

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QLabel, QMessageBox

from res.components.pyqt_toast.toast import Toast
from res.layout.MemberLayout import Ui_Form
from src.activity.AddMemberActivity import AddMemberActivity
from src.activity.InfoMemberActivity import InfoMemberActivity
from src.constants.Global import NOI_TRU
from src.model.Member import Member
from src.service.MemberService import MemberService
from src.utils.Notification import confirmMessageBox


class MemberWiget(QMainWindow, Ui_Form):
    def __init__(self, parent=None, context=None):
        super(MemberWiget, self).__init__(context)
        self.setupUi(context)
        self.parent = parent

        self.memberService = MemberService()
        self.page = 1
        self.count = 0
        self.list = []

        self.toast = Toast(text="", duration=2, parent=self.parent)

        self.tbMember.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbMember.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.handelEvent()
        self.loadData()

    def handelEvent(self):
        self.btnAddMember.clicked.connect(self.addMember)
        self.tbMember.clicked.connect(self.on_cell_clicked)
        self.btnBackPage.clicked.connect(self.backPage)
        self.btnNextPage.clicked.connect(self.nextPage)
        self.edtSearchMemberNT.textChanged.connect(self.search)

    def search(self):
        key = self.edtSearchMemberNT.text()
        if key == "":
            self.loadData()
            return
        self.list = self.memberService.search(key, 1, 100, NOI_TRU)
        self.loadData(self.list)
        self.page = 1
        self.count = 0

    def nextPage(self):
        self.page += 1
        if self.page >= self.totalPage:
            self.page = int(self.totalPage)
            return
        self.loadData()

    def backPage(self):

        self.page -= 1

        if self.page < 1:
            self.page = 1
            return
        self.loadData()

    def on_cell_clicked(self, item):
        # Lấy giá trị của ô được click và in ra màn hình
        index = item.row()
        if index >= len(self.list):
            return
        member = self.list[index]
        self.infoMemberActivity = InfoMemberActivity(parent=self, mainParent=self.parent, member=member)
        self.infoMemberActivity.show()
        self.infoMemberActivity.reloadSignal.connect(self.reloadData)


    def reloadData(self,check):
        if check is False:
           self.loadData()
        else:
            self.loadData(self.list)

    def addMember(self):
        self.addMemberActivity = AddMemberActivity(parent=self, mainParent=self.parent)
        self.addMemberActivity.show()


    def loadData(self, list=None):
        # clear table
        self.tbMember.setRowCount(0)
        if list is None:
            self.list = self.memberService.getPage(self.page, 100, NOI_TRU)
            self.total = self.memberService.getTotal(NOI_TRU)
        else:
            self.list = list
            self.total = len(list)
        self.lbTottal.setText("Tổng: " + str(self.total))
        self.totalPage = self.total / 100
        if self.total % 100 != 0:
            self.totalPage += 1

        self.lbPage.setText("Trang: " + str(int(self.page)) + "/" + str(int(self.totalPage)))

        row = 0
        self.count = int(self.page * 100 - 100)
        self.tbMember.setRowCount(len(self.list))
        for item in self.list:
            self.tbMember.setRowHeight(row, 100)

            self.tbMember.setItem(row, 0, QtWidgets.QTableWidgetItem(str(self.count + 1)))
            # set center
            self.tbMember.item(row, 0).setTextAlignment(Qt.AlignCenter)

            self.tbMember.setItem(row, 1, QtWidgets.QTableWidgetItem(self.getText(item.FullName)))
            self.tbMember.setItem(row, 2, QtWidgets.QTableWidgetItem(self.getText(item.CCCD)))
            address = ""
            if item.Ward != None and item.Ward != "":
                address += item.Ward
            if item.District != None and item.District != "":
                address += "," + item.District
            if item.Province != None and item.Province != "":
                address += "," + item.Province

            self.tbMember.setItem(row, 3, QtWidgets.QTableWidgetItem(self.getText(address)))
            self.tbMember.setItem(row, 4, QtWidgets.QTableWidgetItem(self.getText(item.Relatives)))
            self.tbMember.setItem(row, 5, QtWidgets.QTableWidgetItem(self.getText(item.DateIn)))
            image = QtGui.QImage()
            url = item.Avatar
            if url == None or url == "":
                url = "res/drawable/icons/vatar.jpg"
            pixmap = QPixmap(url)
            pixmap = pixmap.scaled(90, 90, Qt.KeepAspectRatio, Qt.FastTransformation)
            image = QLabel()
            image.setPixmap(pixmap)

            self.tbMember.setCellWidget(row, 6, image)
            # set center
            self.tbMember.cellWidget(row, 6).setAlignment(Qt.AlignCenter)

            iconDelete = QIcon("res/drawable/icons/delete_red_icon.svg")
            btnDelete = QtWidgets.QPushButton()
            btnDelete.setIcon(iconDelete)
            btnDelete.setStyleSheet("background-color: transparent")
            # set size
            btnDelete.setIconSize(QtCore.QSize(24, 24))
            # set pointer
            btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            btnDelete.clicked.connect(lambda _, r=row, item=item: self.on_delete_clicked(r, item))

            self.tbMember.setCellWidget(row, 7, btnDelete)

            row += 1
            self.count += 1

    def on_delete_clicked(self, row, item):
        returnValue, msgBox = confirmMessageBox("Xóa thành viên", "Bạn có chắc muốn xóa thành viên này không?")
        if returnValue == QMessageBox.Ok:
            self.memberService.remove(item.ID, Member)
            self.loadData()
            self.toast.showToast("Xóa thành viên thành công", type=Toast.ERROR)


    def getText(self, text):
        if text == None or text == "":
            return "Chưa có thông tin"
        return text
