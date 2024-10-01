import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt03.ui", self)

        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.calculate_product)

    def calculate_product(self):
        # le1과 le2의 값을 숫자로 변환하여 곱한 후 le3에 설정
        try:
            value1 = int(self.le1.text())  # le1에 입력된 값
            value2 = int(self.le2.text())  # le2에 입력된 값
            result = value1 * value2       # 곱셈 연산
            self.le3.setText(str(result))  # 결과를 le3에 출력
        except ValueError:
            self.le3.setText("Error")      # 숫자가 아닌 값이 들어오면 에러 출력

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
