class Animal:
    def __init__(self):
        self.cnt_hair = 80000
    def eatWell(self):
        self.cnt_hair += 100


if __name__ == '__main__':
    ani = Animal()
    print("cnt_hair", ani.cnt_hair)
    ani.eatWell()
    print("cnt_hair", ani.cnt_hair)




