from random import random
arr =[1,2,3]

for i in range(100):
    swap = arr[0]
    rnd = int(random()*3)
    arr[0] = arr[rnd]
    arr[rnd] = swap
print(arr)




