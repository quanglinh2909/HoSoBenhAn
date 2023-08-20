
from PyQt5.QtWidgets import QMessageBox

def messageBox(error):
    msgBox = QMessageBox()
    msgBox.setStyleSheet("""QMessageBox {background-color: white; border-radius: 5px;} QLabel {background-color: white; color: black; font: 11pt "Open Sans";}
                            QPushButton {background-color: black; color: white; font: 11pt "Open Sans"; border-radius: 5px; width: 60px; height: 25px}""")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(str(error) + ".")
    msgBox.setWindowTitle("Thông báo")
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        msgBox.close()

def messageBoxSuccess(mess):
    msgBox = QMessageBox()
    msgBox.setStyleSheet("""QMessageBox {background-color: white; border-radius: 5px;} QLabel {background-color: white; color: black; font: 11pt "Open Sans";}
                            QPushButton {background-color: black; color: white; font: 11pt "Open Sans"; border-radius: 5px; width: 60px; height: 25px}""")
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setText(str(mess) + ".")
    msgBox.setWindowTitle("Thành công")
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        msgBox.close()

def confirmMessageBox(title,confirm):
    msgBox = QMessageBox()
    msgBox.setStyleSheet("""QMessageBox {background-color: white; border-radius: 5px;} QLabel {background-color: white; color: black; font: 11pt "Open Sans";}
                               QPushButton {background-color: #fff; color: #000; font: 11pt "Open Sans"; border-radius: 5px; width: 100px; height: 25px}""")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.setText( str(confirm))
    msgBox.setWindowTitle(title)
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #set focus button
    msgBox.button(QMessageBox.Ok).setFocus()
    returnValue = msgBox.exec()
    return returnValue, msgBox
