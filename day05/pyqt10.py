import sys
from random import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt10.ui", self)

        self.pb_call.clicked.connect(self.calling)

        self.pb1.clicked.connect(self.add_1)
        self.pb2.clicked.connect(self.add_2)
        self.pb3.clicked.connect(self.add_3)
        self.pb4.clicked.connect(self.add_4)
        self.pb5.clicked.connect(self.add_5)
        self.pb6.clicked.connect(self.add_6)
        self.pb7.clicked.connect(self.add_7)
        self.pb8.clicked.connect(self.add_8)
        self.pb9.clicked.connect(self.add_9)
        self.pb0.clicked.connect(self.add_0)

    def add_1(self):
        self.le.setText(self.le.text() + "1")




    def addNum(self, num):
        current_text = self.le.text()
        self.le.setText(current_text + num)




    def calling(self):
        QMessageBox.question(self.window, 'Message', 'calling', QMessageBox.Yes, QMessageBox.NoButton)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
