import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        lcd = QLCDNumber(self) #슬로
        dial = QDial(self)#시그널

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addWidget(vbox)

        dial.valueChanged.connect(lcd.display)

        self.setGeometry(50,50,200,200)
        self.show()