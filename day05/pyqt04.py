import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt04.ui", self)

        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.play_game)

    def play_game(self):
        # 사용자 입력값 가져오기
        user_input = self.le_input.text().strip().lower()  # 공백 제거하고 소문자로 변환


        # 사용자 입력을 le_mine에 매핑
        self.le_mine.setText(user_input)

        # 컴퓨터가 1부터 100까지 랜덤 숫자를 선택
        computer_number = random.randint(1, 100)
        self.le_com.setText(str(computer_number))

        # 컴퓨터 숫자가 홀수인지 짝수인지 계산
        if computer_number % 2 == 0:
            computer_choice = "짝"
        else:
            computer_choice = "홀"

        # 결과 계산
        if user_input == computer_choice:
            result = "이김"
        else:
            result = "짐"

        # 결과를 le_result에 표시
        self.le_result.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
