from random import random

def getHJ():

    ret = "홀"
    rnd =random()
    if rnd > 0.5:
        ret = "짝"
    return ret

com = getHJ()

print ("com", com)