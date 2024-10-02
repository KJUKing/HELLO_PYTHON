import sys
from random import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt06.ui", self)

        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.play_lotto)

    def play_lotto(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
               21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
               31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
               41, 42, 43, 44, 45
               ]

        for i in range(1000):
            swap = arr[0]
            rnd = int(random() * 45)
            arr[0] = arr[rnd]
            arr[rnd] = swap
        print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])

        for i in range(6):
            for j in range(6):
                if arr[i] < arr[j]:
                    a =arr[i]
                    b =arr[j]
                    arr[i] = b
                    arr[j] = a
        print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])

        self.lcd01.display(arr[0])
        self.lcd02.display(arr[1])
        self.lcd03.display(arr[2])
        self.lcd04.display(arr[3])
        self.lcd05.display(arr[4])
        self.lcd06.display(arr[5])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
