import os

import uuid
import webbrowser
from datetime import datetime

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QDialog, QMainWindow
from dotenv import load_dotenv

from res.components.Loading import LoadingWidget
from res.components.pyqt_toast.toast import Toast
from res.layout.InfoMemberLayout import Ui_MainWindow
from src.activity.EditMemberActivity import EditMemberActivity
from src.constants.Global import NOI_TRU, NGOAI_TRU, MANAGER, DOCTOR
from src.service.ConfigService import ConfigService
from src.service.MemberService import MemberService
from src.utils.comon import readImage
from src.utils.ecportPDF import write_to_pdf_with_image_and_content


class InfoMemberActivity(QMainWindow, Ui_MainWindow):
    reloadSignal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None, mainParent=None, member=None):
        super(InfoMemberActivity, self).__init__(parent)
        self.setupUi(self)
        self.showMaximized()
        self.isEdit = 'False'
        self.configService = ConfigService()
        self.loadingWidget = LoadingWidget(self)
        self.loadingWidget.startLoading()

        # load_dotenv()

        self.isServert = os.getenv('IS_SEVER')

        self.setWindowTitle("Thông tin bệnh nhân")
        self.parent = parent
        self.member = member

        self.listTrieuChung = dict()
        self.listBenhLyKhac = dict()
        self.listThuocDieuTri = dict()
        self.initUi()


        self.handleEvent()



    def handleEvent(self):
        self.btnBack.clicked.connect(self.closeWin)
        self.btnEdit.clicked.connect(self.edit)
        self.btnExport.clicked.connect(self.export)
        self.btnPrint.clicked.connect(self.print)

    def print(self):
        self.loadingWidget.startLoading()
        self.loadingPrint = LoadingPrint(self)
        self.loadingPrint.printSignal.connect(self.printSignal)
        self.loadingPrint.start()
    def printSignal(self, isSuccess):
        self.loadingWidget.stopTopLoading()


    def export(self):
        options = QtWidgets.QFileDialog.Options()

        fileName = self.member.FullName + ".pdf"
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", fileName,
                                                            "PDF (*.pdf)", options=options)
        if fileName:
            nameManager = self.configService.getByKey(MANAGER)
            nameDoctor = self.configService.getByKey(DOCTOR)
            if nameManager is None:
                nameManager = ""
            else:
                nameManager = nameManager.Value

            if nameDoctor is None:
                nameDoctor = ""
            else:
                nameDoctor = nameDoctor.Value

            write_to_pdf_with_image_and_content(fileName, self.member, nameManager, nameDoctor)

    def edit(self):
        self.editMemberActivity = EditMemberActivity(parent=self, mainParent=self.parent, member=self.member)
        self.editMemberActivity.show()
        self.editMemberActivity.reloadSignal.connect(self.reload)

    def reload(self, memeber=None):
        if self.member.Type != memeber.Type:
            self.isEdit = "ChangeType"
        self.initUi(memeber)
        self.isEdit = 'True'

    def closeWin(self):
        self.close()

    def closeEvent(self, event):
        if self.isEdit == 'True':
            self.reloadSignal.emit(False)
        if self.isEdit == 'ChangeType':
            self.parent.reloadSignal.emit(True)
        event.accept()

    def clearLayOut(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def getAddress(sleft, member):
        address = ""
        if member.Address != None and member.Address != "":
            address += member.Address
        if member.Ward != None and member.Ward != "":
            address += ", " + member.Ward
        if member.District != None and member.District != "":
            address += ", " + member.District
        if member.Province != None and member.Province != "":
            address += ", " + member.Province
        return address

    def initUi(self, memeber=None):
        if memeber != None:
            self.member = memeber
        self.clearLayOut(self.verticalLayout_6)
        self.clearLayOut(self.verticalLayout_21)
        self.clearLayOut(self.verticalLayout_19)
        self.lbName.setText(self.getText(self.member.FullName))
        self.lbBirday.setText(self.getText(self.member.Birthday))
        self.lbCCCD.setText(self.getText(self.member.CCCD))
        self.lbNameRelatives.setText(self.getText(self.member.Relatives))
        self.lbInfoRelatives.setText(self.getText(self.member.InfoRelatives))
        self.lbDateIn.setText(self.getText(self.member.DateIn))
        self.lbAccommodation.setText(self.getAddress(self.member))
        type = self.member.Type
        if type == NGOAI_TRU:
            type = "Ngoại trú"
        elif type == NOI_TRU:
            type = "Nội trú"
        else:
            type = "Chưa có thông tin"
        self.lbType.setText(type)

        self.lbCDB.setText("- " + self.getText(self.member.CDB))
        self.lbNote.setText("- " + self.getText(self.member.Note))

        CN = self.member.CN
        DH = self.member.DH
        HA = self.member.HA
        listCN = CN.split('*&**&*')
        listHD = DH.split('*&**&*')
        listHP = HA.split('*&**&*')
        for i in range(12):
            cn = self.findChild(QtWidgets.QLabel, "lbCN" + str(i + 1))
            dh = self.findChild(QtWidgets.QLabel, "lbDH" + str(i + 1))
            ha = self.findChild(QtWidgets.QLabel, "lbHA" + str(i + 1))
            if i < len(listCN):
                cn.setText(listCN[i])
            if i < len(listHD):
                dh.setText(listHD[i])
            if i < len(listHP):
                ha.setText(listHP[i])

        Medicine = self.getText(self.member.Medicine)
        Symptoms = self.getText(self.member.Symptoms)
        OtherMedicalConditions = self.getText(self.member.OtherMedicalConditions)
        listMedicine = Medicine.split('*&**&*')
        listSymptoms = Symptoms.split('*&**&*')
        listOtherMedicalConditions = OtherMedicalConditions.split('*&**&*')
        for i in range(len(listSymptoms) - 1):
            self.addItem(self.frame_5, self.verticalLayout_6, self.listTrieuChung)
            if i < len(listSymptoms) and listSymptoms[i] != "":
                self.listTrieuChung[list(self.listTrieuChung.keys())[i]].setText("- " + listSymptoms[i])

        for i in range(len(listOtherMedicalConditions) - 1):
            self.addItem(self.frame_13, self.verticalLayout_19, self.listBenhLyKhac)
            if i < len(listOtherMedicalConditions) and listOtherMedicalConditions[i] != "":
                self.listBenhLyKhac[list(self.listBenhLyKhac.keys())[i]].setText("- " + listOtherMedicalConditions[i])

        for i in range(len(listMedicine) - 1):
            self.addItem(self.frame_18, self.verticalLayout_21, self.listThuocDieuTri)
            if i < len(listMedicine) and listMedicine[i] != "":
                self.listThuocDieuTri[list(self.listThuocDieuTri.keys())[i]].setText("- " + listMedicine[i])

        if int(self.isServert) == 1:
            urlAvatar = self.member.Avatar
            if os.path.exists(urlAvatar) and os.path.isfile(urlAvatar):
                self.label.setPixmap(QtGui.QPixmap(urlAvatar))
            self.loadingWidget.stopTopLoading()
        else:
            self.l = Loading(member=self.member)
            self.l.start()
            self.l.imageSignal.connect(self.loadImagge)


    def loadImagge(self,p):
        if p is not None:
            self.label.setPixmap(QtGui.QPixmap(p))
        self.loadingWidget.stopTopLoading()


    def getText(self, text):
        if text == None or text == "":
            return "Chưa có thông tin"
        return text

    def addItem(self, layout, verticalLayout, list):
        id = uuid.uuid4().hex
        list[id] = QtWidgets.QLabel(layout)
        font = QtGui.QFont()
        font.setPointSize(12)
        list[id].setFont(font)
        list[id].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        list[id].setWordWrap(True)
        list[id].setObjectName(id)
        verticalLayout.addWidget(list[id])

class Loading(QThread):
    imageSignal = pyqtSignal(object)
    def __init__(self, member=None):
        super(Loading, self).__init__()
        self.member = member

    def run(self):
        urlAvatar = self.member.Avatar
        p = readImage(urlAvatar)
        self.imageSignal.emit(p)

class LoadingPrint(QThread):
    printSignal = pyqtSignal(bool)
    def __init__(self, parent=None):
        super(LoadingPrint, self).__init__(parent)
        self.configService = ConfigService()
        self.parent = parent
    def run(self):

       try:
           nameManager = self.configService.getByKey(MANAGER)
           nameDoctor = self.configService.getByKey(DOCTOR)
           if nameManager is None:
               nameManager = ""
           else:
               nameManager = nameManager.Value

           if nameDoctor is None:
               nameDoctor = ""
           else:
               nameDoctor = nameDoctor.Value
           write_to_pdf_with_image_and_content("assets/print.pdf", self.parent.member, nameManager, nameDoctor)
           # get the path of the current directory
           current_dir = os.getcwd()
           urlFile = current_dir + "/assets/print.pdf"
           webbrowser.open(urlFile)
           self.printSignal.emit(True)
       except Exception as e:
              print(e)
              self.printSignal.emit(False)

