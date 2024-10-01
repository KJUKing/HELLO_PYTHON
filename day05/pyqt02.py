import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ui 파일 불러오기
        uic.loadUi("pyqt02.ui", self)

        # 버튼 클릭 시 실행될 메서드 연결
        self.pb.clicked.connect(self.increase_value)

    def increase_value(self):
        # QLineEdit에 있는 텍스트 값을 숫자로 변환한 후 1 증가
        current_value = int(self.lineEdit.text())
        new_value = current_value + 1
        # 증가한 값을 다시 QLineEdit에 설정
        self.lineEdit.setText(str(new_value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
