import os

import uuid
from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QMainWindow
from dotenv import load_dotenv

from res.components.Loading import LoadingWidget
from res.components.pyqt_toast.toast import Toast
from res.layout.AddMemberLayout import Ui_MainWindow
from src.constants.Global import NOI_TRU, NGOAI_TRU
from src.model.Member import Member
from src.service.MemberService import MemberService
from src.utils.comon import uploadfile


class AddMemberActivity(QMainWindow, Ui_MainWindow):
    loadDataSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None, mainParent=None):
        super(AddMemberActivity, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.loadingWidget = LoadingWidget(self)

        self.setWindowTitle("Thêm bệnh nhân")
        self.parent = parent
        self.streamVideo = None
        self.listTrieuChung = dict()
        self.listBenhLyKhac = dict()
        self.listThuocDieuTri = dict()
        self.urlIMage = "res/drawable/icons/vatar.jpg"
        self.memberService = MemberService()

        self.initUi()
        self.handleEvent()
        self.toast = Toast(text="", duration=2, parent=self)

    def initUi(self):
        self.clearLayOut(self.verticalLayout_6)
        self.clearLayOut(self.verticalLayout_15)
        self.clearLayOut(self.verticalLayout_9)
        self.addItem(self.frame_5, self.verticalLayout_6, self.listTrieuChung)
        self.addItem(self.frame_76, self.verticalLayout_15, self.listBenhLyKhac)
        self.addItem(self.frame_92, self.verticalLayout_9, self.listThuocDieuTri)

        # set dateEditIn now
        self.dateEditIn.setDate(QtCore.QDate.currentDate())

    def handleEvent(self):
        self.btnBack.clicked.connect(self.closeWin)
        # self.btnAddCamera.clicked.connect(self.save)
        # self.btnRunTestCamera.clicked.connect(self.runTestCamera)
        self.btnAddTrieuChung.clicked.connect(
            lambda: self.addItem(self.frame_5, self.verticalLayout_6, self.listTrieuChung))
        self.btnBenhLyKhac.clicked.connect(
            lambda: self.addItem(self.frame_76, self.verticalLayout_15, self.listBenhLyKhac))
        self.btnThuocDieuTri.clicked.connect(
            lambda: self.addItem(self.frame_92, self.verticalLayout_9, self.listThuocDieuTri))

        self.btnSave.clicked.connect(self.save)
        self.btnEditImage.clicked.connect(self.openSelectImage)
        self.btnDeleteIMage.clicked.connect(self.deleteImage)

    def deleteImage(self):
        self.labelImage.clear()
        self.urlIMage = "res/drawable/icons/vatar.jpg"
        self.labelImage.setPixmap(QtGui.QPixmap(self.urlIMage))

    def openSelectImage(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image", "",
                                                            "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio)
            self.labelImage.setPixmap(pixmap)
            self.labelImage.setScaledContents(True)
            self.urlIMage = fileName

    def save(self):
        listTextTrieuChung = self.getListText(self.listTrieuChung)
        listTextBenhLyKhac = self.getListText(self.listBenhLyKhac)
        listTextThuocDieuTri = self.getListText(self.listThuocDieuTri)

        name = self.lineEditName.text().strip()
        birthday = self.dateEditBriday.date().toString("dd/MM/yyyy")
        cccd = self.lineEditCCCD.text().strip()
        nameRelatives = self.lineEditRelatives.text().strip()
        infoRelatives = self.lineEditInfoRelatives.toPlainText().strip()
        dateIn = self.dateEditIn.date().toString("dd/MM/yyyy")

        province = self.lineEditProvince.text().strip()
        district = self.lineEditDistrict.text().strip()
        ward = self.lineEditWards.text().strip()
        address = self.lineEditAddress.text().strip()

        chuanDoanBenh = self.textEditCDB.toPlainText().strip()
        note = self.textEditNote.toPlainText().strip()

        type = self.comboBox.currentText().strip()
        if type == "Nội trú":
            type = NOI_TRU
        else:
            type = NGOAI_TRU

        if name == "":
            self.toast.showToast("Vui lòng nhập tên bệnh nhân", type=Toast.ERROR)
            return

        cnResult = ""
        dhResult = ""
        haResult = ""
        for i in range(12):
            cn = self.findChild(QtWidgets.QPlainTextEdit, "plainTextEditCN" + str(i + 1))
            dh = self.findChild(QtWidgets.QPlainTextEdit, "plainTextEditDH" + str(i + 1))
            ha = self.findChild(QtWidgets.QPlainTextEdit, "plainTextEditHA" + str(i + 1))
            cnResult += cn.toPlainText().strip() + "*&**&*"
            dhResult += dh.toPlainText().strip() + "*&**&*"
            haResult += ha.toPlainText().strip() + "*&**&*"

        # convert thuoc dieu tri to string
        thuocDieuTri = ""
        for i in range(len(listTextThuocDieuTri)):
            thuocDieuTri += listTextThuocDieuTri[i] + "*&**&*"

        # convert benh ly khac to string
        benhLyKhac = ""
        for i in range(len(listTextBenhLyKhac)):
            benhLyKhac += listTextBenhLyKhac[i] + "*&**&*"

        # convert trieu chung to string
        trieuChung = ""
        for i in range(len(listTextTrieuChung)):
            trieuChung += listTextTrieuChung[i] + "*&**&*"

        id = uuid.uuid4().hex
        member = Member(ID=id, FullName=name, Birthday=birthday, CCCD=cccd, Relatives=nameRelatives,
                        InfoRelatives=infoRelatives, DateIn=dateIn, Province=province, District=district, Ward=ward,
                        Address=address, CDB=chuanDoanBenh, Note=note, CN=cnResult, DH=dhResult,
                        HA=haResult, OtherMedicalConditions=benhLyKhac, Symptoms=trieuChung, Medicine=thuocDieuTri,
                        Type=type)
        self.loadingWidget.startLoading()
        self.loadingSave = LoadingSave(member, self.urlIMage)
        self.loadingSave.start()
        self.loadingSave.imageSignal.connect(self.saveSuccess)

    def saveSuccess(self, member):
        self.loadingWidget.stopTopLoading()
        if member is not None:
            self.close()
            self.parent.parent.parent.toast.showToast("Thêm thành công", type=Toast.SUCCESS)
            self.loadDataSignal.emit()
        else:
            self.toast.showToast("Thêm thất bại", type=Toast.ERROR)

    def getUrl(self):
        pathRoot = "assets/images/"
        if not os.path.exists(pathRoot):
            os.makedirs(pathRoot)
        date = datetime.now()
        path = pathRoot + date.strftime("%Y%m%d")
        if not os.path.exists(path):
            os.makedirs(path)
        name = uuid.uuid4().hex
        path = path + "/" + name + "_" + date.strftime("%H%M%S") + ".jpg"
        return path

    def clearLayOut(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def closeEvent(self, event):
        event.accept()

    def closeWin(self):
        self.close()

    def addItem(self, layout, verticalLayout, list):
        id = uuid.uuid4().hex
        list[id] = QtWidgets.QFrame(layout)
        list[id].setMinimumSize(QtCore.QSize(0, 40))
        list[id].setFrameShape(QtWidgets.QFrame.StyledPanel)
        list[id].setFrameShadow(QtWidgets.QFrame.Raised)
        list[id].setObjectName(id)
        horizontalLayout_13 = QtWidgets.QHBoxLayout(list[id])
        horizontalLayout_13.setContentsMargins(9, 0, 0, 0)
        horizontalLayout_13.setObjectName("horizontalLayout")
        btnDelete = QtWidgets.QPushButton(list[id])
        btnDelete.setMinimumSize(QtCore.QSize(30, 30))
        btnDelete.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(62)
        btnDelete.setFont(font)
        btnDelete.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        btnDelete.setStyleSheet("color:#fff;\n"
                                "font-weight:500;\n"
                                "border-radius: 5px;\n"
                                "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/res/drawable/icons/delete_red_icon.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        btnDelete.setText("")
        btnDelete.setIcon(icon1)
        btnDelete.setIconSize(QtCore.QSize(24, 24))
        btnDelete.setObjectName("btnDelete")
        horizontalLayout_13.addWidget(btnDelete)
        lineEdit_2 = QtWidgets.QLineEdit(list[id])
        lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 35))
        lineEdit_2.setObjectName("lineEdit_2")
        horizontalLayout_13.addWidget(lineEdit_2)
        verticalLayout.addWidget(list[id])
        # _translate = QtCore.QCoreApplication.translate
        # lineEdit_2.setPlaceholderText(_translate("Dialog", "Nhập triệu chứng bệnh..."))
        btnDelete.clicked.connect(lambda: self.deleteItem(id, list))

    def deleteItem(self, id, list):
        list[id].deleteLater()
        del list[id]

    def getListText(self, list):
        result = []
        for key in list:
            if list[key].findChild(QtWidgets.QLineEdit).text().strip() != "":
                result.append(list[key].findChild(QtWidgets.QLineEdit).text())
        return result


class LoadingSave(QThread):
    imageSignal = pyqtSignal(object)

    def __init__(self, member=None, urlIMage=None):
        super(LoadingSave, self).__init__()
        self.member = member
        self.urlIMage = urlIMage
        self.memberService = MemberService()

    def run(self):
        try:
            url = self.member.Avatar
            if self.member.Avatar != self.urlIMage:
                url = uploadfile(self.urlIMage)
            self.member.Avatar = url
            res = self.memberService.create(self.member)
            if res:
                self.imageSignal.emit(self.member)
            else:
                self.imageSignal.emit(None)
        except Exception as e:
            print('Error: ', e)
            self.imageSignal.emit(None)

