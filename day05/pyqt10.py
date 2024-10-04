import sys
from random import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt10.ui", self)

        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)


        self.pb_call.clicked.connect(self.mycall)

    def mycall(self):
        str_tel = self.le.text()
        QMessageBox.about(self, 'calling', str_tel)

    def myclick(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        self.le.setText(str_old+str_new)


    def calling(self):
        QMessageBox.question(self.window, 'Message', 'calling', QMessageBox.Yes, QMessageBox.NoButton)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
