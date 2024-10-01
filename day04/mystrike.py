
def getS(mine, com):

    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]

    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]

    ret = 0;
    if m1 == c1:
        ret+=1
    if m2 == c2:
        ret+=1
    if m3 == c3:
        ret+=1

    return ret


def getB(mine, com):

    m1 = mine[0:1]
    m2 = mine[1:2]
    m3 = mine[2:3]

    c1 = com[0:1]
    c2 = com[1:2]
    c3 = com[2:3]

    ret = 0;
    if m1 == c2 or m1 == c3 :
        ret+=1
    if m2 == c1 or m2 == c3 :
        ret+=1
    if m3 == c1 or m3 == c2:
        ret+=1

    return ret

def ran3():
    from random import random
    arr =[1,2,3,4,5,6,7,8,9]

    for i in range(100):
        swap = arr[0]
        rnd = int(random()*9)
        arr[0] = arr[rnd]
        arr[rnd] = swap

    return "{}{}{}".format(arr[0],arr[1],arr[2])

com = ran3()

cnt = 0
while True:
    mine = input("맞춰보세요")
    s = getS(mine, com)
    b = getB(mine, com)
    print("{}\t{}S{}B".format(mine,s,b))
    if s == 3:
        print("맞췄습니다")
        break
    print("s",s,"b",b)
    cnt += 1
    if cnt >= 10:
        print("실패했습니다")
        break