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
        user_input = self.le_input.text().strip()
        valid_choices = ["가위", "바위", "보"]

        if user_input not in valid_choices:
            self.le_result.setText("올바른 값을 입력하세요: 가위, 바위, 보")
            return

        # 사용자 입력을 le_mine에 매핑
        self.le_mine.setText(user_input)

        # 컴퓨터 선택 (랜덤)
        computer_choice = random.choice(valid_choices)
        self.le_com.setText(computer_choice)

        # 결과 계산
        if user_input == computer_choice:
            result = "비김"
        elif (user_input == "가위" and computer_choice == "보") or \
                (user_input == "바위" and computer_choice == "가위") or \
                (user_input == "보" and computer_choice == "바위"):
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