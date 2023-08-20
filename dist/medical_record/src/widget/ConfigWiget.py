import uuid

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QTableWidgetItem, QLabel

from res.components.pyqt_toast.toast import Toast
from res.layout.ConfigLayout import Ui_Form
from src.constants.Global import IS_SERVER, MANAGER, DOCTOR
from src.model.Config import Config
from src.service.ConfigService import ConfigService
from src.utils.Notification import confirmMessageBox

from src.widget.MemberWiget import MemberWiget
from src.widget.MemberWigetBT import MemberWigetBT


class ConfigWiget(QMainWindow, Ui_Form):
    def __init__(self, parent=None, context=None):
        super(ConfigWiget, self).__init__(context)
        self.setupUi(context)
        self.parent = parent
        self.configService = ConfigService()
        self.toast = Toast(text="", duration=2, parent=self.parent)
        self.initUi()

        self.handleEvent()

    def initUi(self):
        managerGetBykey = self.configService.getByKey(MANAGER)
        doctorGetBykey = self.configService.getByKey(DOCTOR)
        isServerGetBykey = self.configService.getByKey(IS_SERVER)

        if managerGetBykey is not None:
            self.lineEditManager.setText(managerGetBykey.Value)
        if doctorGetBykey is not None:
            self.lineDoctor.setText(doctorGetBykey.Value)


    def handleEvent(self):
        self.btnSave.clicked.connect(self.save)

    def save(self):
        nameManager = self.lineEditManager.text().strip()
        nameDoctor = self.lineDoctor.text().strip()



        managerGetBykey = self.configService.getByKey(MANAGER)
        doctorGetBykey = self.configService.getByKey(DOCTOR)

        if managerGetBykey is None:
            id = uuid.uuid4().hex
            manager = Config(Key=MANAGER, Value=nameManager, ID=id)
            self.configService.create(manager)
        else:
            managerGetBykey.Value = nameManager
            self.configService.update(managerGetBykey)

        if doctorGetBykey is None:
            id = uuid.uuid4().hex
            doctor = Config(Key=DOCTOR, Value=nameDoctor, ID=id)
            self.configService.create(doctor)
        else:
            doctorGetBykey.Value = nameDoctor
            self.configService.update(doctorGetBykey)

        # if isServerGetBykey is None:
        #     id = uuid.uuid4().hex
        #     self.configService.create(isServer)
        # else:
        #     check = False
        #     if isServerGetBykey.Value != server:
        #         check = True
        #     isServerGetBykey.Value = server
        #     self.configService.update(isServerGetBykey)
        #     if check:
        #         returnValue, msgBox = confirmMessageBox("Khởi động ứng dụng",
        #                                                 "Bạn đã thay đổi cấu hình máy chủ, ứng dụng sẽ khởi động lại để cập nhật cấu hình.")
        #         self.parent.close()

        self.toast.showToast("Lưu thành công", Toast.SUCCESS)
