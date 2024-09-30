from day04.car import car


class yumo(car):

    def __init__(self):
        super().__init__()
        self.flagBaby = True
        print("생성자")

    def grownUp(self):
        self.flagBaby = False

    def __del__(self):
        print("소멸자")



