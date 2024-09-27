# 가위/바위/보를 선택하세요

# 나 :가위
# 컴 :가위,바위,보
# 결과 : 비김,짐,이김

from random import random


def sci_roc_pap(mine):
    # com = int(random()*3)
    # print(com)
    print("나 :", mine)
    print("컴 : 가위, 바위, 보")
    if mine=="가위":
        return "비김","짐","이김"
    elif mine=="바위":
        return "이김","비김","짐"
    elif mine=="보":
        return "짐","이김","비김"
    else:
        print("잘못된거 입력함")


print(sci_roc_pap(input("가위바위보 중 입력하세요")))
