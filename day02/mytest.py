# 첫수를 입력하세요 1
# 끝수를 입력하세요 4
# 1에서부터 4까지의 합은

a = input("첫 수를 입력하세요")
b = input("둘째 수를 입력하세요")

print(a+"에서부터 " + b +"까지의 합은")

arr = range(int(a), int(b)+1)

sum =0

for i in arr:
    sum += i

print(sum)