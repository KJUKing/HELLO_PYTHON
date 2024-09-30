# 첫별수를 입력하시오 3
# 끝별수를 입력하시오 5

# ***
# ****
# *****
def star(cnt):
    ret = ""
    for i in range(cnt):
        ret += "*"
    return ret

f = input("첫 별수를 입력하시오")
l = input("끝 별수를 입력하시오")
ff = int(f)
ll = int(l)

for i in range(ff, ll+1):
    print(star(i))
