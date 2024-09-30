# 첫별수를 입력하시오 3
# 끝별수를 입력하시오 7
# 배수를 입력하시오 3
# 3과 7사이의 3의 배수의 합은 9입니다

f = input("첫수를 입력하시오")
l = input("끝수를 입력하시오")
m = input("배수를 입력하시오")
ff = int(f)
ll = int(l)
mm = int(m)
sum = 0
for i in range(ff, ll+1, mm):
    if i%mm == 0:
       sum += i

print("{}과 {}사이의 {}의 배수의 합은 {}입니다".format(ff, ll, mm, str(sum)))