from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QAbstractAnimation, QPoint
from PyQt5.QtGui import QFont, QColor
# from pyqt_resource_helper import PyQtResourceHelper



class Toast(QWidget):
    NORMAL = 'normal'
    SUCCESS = 'success'
    ERROR = 'error'
    WARNING = 'warning'

    def __init__(self, text, duration=2, parent=None):
        super().__init__(parent)
        self.__initVal(parent, duration)
        self.__initUi(text)

    def __initVal(self, parent, duration):
        self.__parent = parent
        self.__parent.installEventFilter(self)
        self.installEventFilter(self)
        self.__timer = QTimer(self)
        self.__duration = duration
        self.__opacity = 0.9
        self.__foregroundColor = '#ffffff'
        self.__backgroundColor = '#030e16'

    def __initUi(self, text):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        # text in toast (toast foreground)
        self.__lbl = QLabel(text)
        #wrap text
        self.__lbl.setObjectName('popupLbl')
        # PyQtResourceHelper.setStyleSheet([self.__lbl], ['style/foreground.css'])
        self.__lbl.setMinimumWidth(self.__parent.width())
        self.__lbl.setMinimumHeight(self.__lbl.fontMetrics().boundingRect(text).height() * 2)

        self.__lbl.setWordWrap(True)

        # animation
        self.__initAnimation()

        # toast background
        lay = QHBoxLayout()
        lay.addWidget(self.__lbl)
        lay.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # PyQtResourceHelper.setStyleSheet([self], ['style/background.css'])
        self.__setToastSizeBasedOnTextSize()
        self.setLayout(lay)

    def __setOpacity(self, opacity):
        opacity_effect = QGraphicsOpacityEffect(opacity=opacity)
        self.setGraphicsEffect(opacity_effect)

    def __initAnimation(self):
        self.__animation = QPropertyAnimation(self, b"opacity")
        self.__animation.setStartValue(0.0)
        self.__animation.setDuration(200)
        self.__animation.setEndValue(self.__opacity)
        self.__animation.valueChanged.connect(self.__setOpacity)
        self.setGraphicsEffect(QGraphicsOpacityEffect(opacity=0.0))

    def __initTimeout(self):
        self.__timer = QTimer(self)
        self.__timer_to_wait = self.__duration
        self.__timer.setInterval(2000)
        self.__timer.timeout.connect(self.__changeContent)
        self.__timer.start()

    def __changeContent(self):
        self.__timer_to_wait -= 1
        if self.__timer_to_wait <= 0:
            self.__animation.setDirection(QAbstractAnimation.Backward)
            self.__animation.start()
            self.__timer.stop()
            self.hide()

    def setPosition(self, pos):
        geo = self.geometry()
        geo.moveCenter(pos)
        self.setGeometry(geo)

    def showToast(self,text,type="normal"):
        if type == "normal":

            self.setStyleSheet("background-color: #030e16 , color: #ffffff")
        if type == 'success':
            self.setStyleSheet("background-color: green")
        if type == 'error':
            self.setStyleSheet("background-color: red")
        if type == 'warning':
            self.setStyleSheet("background-color: yellow")
        self.__lbl.setText(text)
        self.show()

    def show(self):
        if self.__timer.isActive():
            pass
        else:
            self.__animation.setDirection(QAbstractAnimation.Forward)
            self.__animation.start()
            self.raise_()
            self.__initTimeout()
        return super().show()

    def isVisible(self) -> bool:
        return self.__timer.isActive()

    def setFont(self, font: QFont):
        self.__lbl.setFont(font)
        self.__setToastSizeBasedOnTextSize()

    def __setToastSizeBasedOnTextSize(self):
        self.setFixedWidth(self.__lbl.sizeHint().width() * 2)
        self.setFixedHeight(self.__lbl.sizeHint().height() * 2)

    def setDuration(self, duration: int):
        self.__duration = duration
        self.__initAnimation()

    def setForegroundColor(self, color: QColor):
        if isinstance(color, str):
            color = QColor(color)
        self.__foregroundColor = color.name()

    def setBackgroundColor(self, color: QColor):
        if isinstance(color, str):
            color = QColor(color)
        self.__backgroundColor = color.name()

    def __setForegroundColor(self):
        self.__lbl.setStyleSheet(f'QLabel#popupLbl {{ color: {self.__foregroundColor}; padding: 5px; font: 12pt "Open Sans";}}')
        self.__lbl.setAlignment(QtCore.Qt.AlignCenter)

    def __setBackgroundColor(self):
        self.setStyleSheet(f'QWidget {{ background-color: {self.__backgroundColor}; border-radius: 5px; margin: 0}}')

    def setOpacity(self, opacity: float):
        self.__opacity = opacity
        self.__initAnimation()

    def eventFilter(self, obj, e) -> bool:
        if e.type() == 14:
            self.setPosition(QPoint(self.__parent.width() / 2, self.__parent.height() - self.height() + 30))
            self.setMinimumHeight(100)
        elif isinstance(obj, Toast):
            if e.type() == 75:
                self.__setForegroundColor()
                self.__setBackgroundColor()
        return super().eventFilter(obj, e)