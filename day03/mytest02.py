# 숫자를 맞추세요 5
# UP 5
# 숫자를 맞추세요 60
# DOWN 60
# 숫자를 맞추세요 50
# 정답입니다

# 10번넘어가면 실패하셨습니다 출력
# 횟수는 10번안에 맞춰야함

from random import random

com = int(random() * 99) + 1
print(com)

flag_o = False
for i in range(1, 10 + 1):
    num = int(input("숫자를 맞추세요: "))  # 입력받은 값을 정수로 변환
    if num < com:
        print("UP", num)
    elif num > com:
        print("DOWN", num)
    else:
        print("정답입니다")
        flag_o = True
        break
if not flag_o:
    print("실패하셨습니다")
