# 1~ 10사이의 2배수의 합을 구하시오

arr = range(1, 10+1)

sum =0

for i in arr:
    if i%2 == 0:
        sum += i

print(sum)