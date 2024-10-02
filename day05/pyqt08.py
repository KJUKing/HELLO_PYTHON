import sys
from random import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt08.ui", self)

        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.summary_num)

    def summary_num(self):

        f = int(self.le01.text())
        l = int(self.le02.text())
        m = int(self.le03.text())

        result = 0
        for i in range(f, l+1):
            if i%m ==0:
                result += i
        self.le04.setText(str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
