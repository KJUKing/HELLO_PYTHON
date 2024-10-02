import sys
from random import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt09.ui", self)
        self.com = int(random() * 99) + 1
        print(self.com)

        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.upAndDown)

    def upAndDown(self):
        mine = self.le.text()
        imine = int(mine)
        txt = ""
        if imine < self.com:
            txt = mine + "\t" + "UP\n"
        elif imine > self.com:
            txt = mine + "\t" + "DOWN\n"
        else:
            txt = mine + "\t" + "ANSWER\n"

        txt_old = self.te.toPlainText()
        self.te.setText(txt_old + txt)
        self.le.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
