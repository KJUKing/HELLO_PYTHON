class xijinping:
    def __init__(self):
        self.nuclear = 1000

    def peace(self):
        self.nuclear -= 100
        if(self.nuclear<=0):
            self.nuclear = 0


class JDragon:
    def __init__(self):
        self.money = 15

    def divorce(self):
        self.money /= 2


class chanjuPing(xijinping, JDragon):

    def __init__(self):
        # super().__init__()
        JDragon.__init__(self)
        xijinping.__init__(self)

chanju = chanjuPing()
print(chanju.nuclear)
chanju.peace()
print(chanju.nuclear)

print(chanju.money)
chanju.divorce()
print(chanju.money)





