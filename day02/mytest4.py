#랜덤을 이용하여 홀/짝을 출력하시오

from random import random

rnd = random()

if rnd > 0.5:
    print("홀")
else:
    print("짝")