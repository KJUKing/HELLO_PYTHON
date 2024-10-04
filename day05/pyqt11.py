import sys
from random import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt11.ui", self)

        self.com = self.ran3()
        self.pb.clicked.connect(self.myclick)

    def ran3(self):
        arr = [1,2,3,4,5,6,7,8,9]
        for i in range(100):
            rnd = int(random()*9)
            a = arr[0]
            b = arr[rnd]
            arr[0] =b
            arr[rnd] =a
        return str(arr[0])+str(arr[1])+str(arr[2])

    def getS(self, mine, com):
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]

        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]

        ret = 0
        if c1 == m1: ret += 1
        if c2 == m2: ret += 1
        if c3 == m3: ret += 1

        return ret

    def getB(self, mine, com):
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]

        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]

        ret = 0
        if c1 == m2 or c1 == m3: ret += 1
        if c2 == m1 or c2 == m3: ret += 1
        if c3 == m1 or c3 == m2: ret += 1

        return ret

    def myclick(self):
        mine = self.le.text()
        s = self.getS(mine, self.com)
        b = self.getB(mine, self.com)

        line = "{}\t{}S{}B".format(mine, s, b)
        str_old = self.te.toPlainText()
        self.te.setPlainText(str_old + "\n" +line)
        self.le.setText("")

        if s == 3:
            QMessageBox.about(self, '야구게임', '축하합니다')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
