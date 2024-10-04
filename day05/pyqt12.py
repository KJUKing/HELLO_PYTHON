import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt12.ui", self)

        # 버튼 클릭 시 실행될 메서드 연결

        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)

    def myclick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""

        rnd = random()
        if rnd > 0.66:
            com = "가위"
        elif rnd > 0.33:
            com = "바위"
        else:
            com = "보"

        if com == "가위" and mine == "가위": result = "비김"

        # 결과를 le_result에 표시
        self.le_result.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())