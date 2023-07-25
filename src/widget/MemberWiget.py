from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QLabel

from res.components.pyqt_toast.toast import Toast
from res.layout.MemberLayout import Ui_Form
from src.activity.AddMemberActivity import AddMemberActivity
from src.constants.Global import NOI_TRU
from src.service.MemberService import MemberService


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

    def nextPage(self):
        self.count = int(self.page * 100)
        self.page += 1
        if self.page > self.totalPage:
            self.page = self.totalPage
            return
        self.loadData()

    def backPage(self):
        self.count = int(self.page )

        self.page -= 1

        if self.page < 1:
            self.page = 1
            return
        self.loadData()

    def on_cell_clicked(self, item):
        # Lấy giá trị của ô được click và in ra màn hình
        index = item.row()
        print(f"Clicked value: {index}")

    def addMember(self):
        self.addMemberActivity = AddMemberActivity(parent=self, mainParent=self.parent)
        self.addMemberActivity.show()

    def loadData(self):
        # clear table
        self.tbMember.setRowCount(0)

        self.list = self.memberService.getPage(self.page, 100, NOI_TRU)
        self.total = self.memberService.getTotal(NOI_TRU)
        self.lbTottal.setText("Tổng: " + str(self.total))
        self.totalPage = self.total / 100
        if self.total % 100 != 0:
            self.totalPage += 1

        self.lbPage.setText("Trang: " + str(int(self.page)) + "/" + str(int(self.totalPage)))

        row = 0
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
        print(item.ID)

    def getText(self, text):
        if text == None or text == "":
            return "Chưa có thông tin"
        return text