import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt05.ui", self)


        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.play_gugudan)
        # 엔터키 입력 시 play_gugudan 실행
        self.le.returnPressed.connect(self.play_gugudan)

    def play_gugudan(self):
        # 사용자 입력값 가져오기
        user_input = self.le.text()
        dan = int(user_input)

        # 사용자 입력을 le_mine에 매핑
        self.le.setText(user_input)

        result = ""
        for i in range(1,9+1):
            # 결과를 te에 표시
            result += "{} * {} = {}\n".format(dan, i, dan*i)

        self.te.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())