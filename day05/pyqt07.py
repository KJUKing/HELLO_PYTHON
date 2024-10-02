import sys
from random import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt07.ui", self)

        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.display_star)

    def star(self, cnt):
        result = ""
        ret = ""
        for i in range(cnt):
            ret+= "*"
        ret += "\n"
        return ret

    def display_star(self):

        f = self.sb_first.value()
        l = self.sb_last.value()

        txt = ""
        for i in range(f, l+1):
            txt += self.star(i)

        self.pte.setPlainText(txt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
