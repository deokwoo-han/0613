import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initWindow()


    def initWindow(self):
        lcd = QLCDNumber(self) #슬롯h
        dial = QDial(self)#시그널
        btn1 = QPushButton('BIG', self)
        btn2 = QPushButton('SMALL', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

        self.setGeometry(50,50,200,200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())