# 홀/짝을 선택하시오 홀
# 나 : 홀
# 컵 : 홀 / 짝
# 결과 : 승리 / 패배

from random import random

rnd = random()

my = input("홀/짝을 선택하시오")


if rnd > 0.5:
    cup = "홀"
else:
    cup = "짝"

    print("나 : " + my)
    print("컵 : " + cup)


if my == cup:
    print("승리")
else:
    print("패배")

