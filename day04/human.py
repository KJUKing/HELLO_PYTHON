from day04.animal import Animal


class Human(Animal):
    def __init__(self):
        super().__init__()
        self.lang = 0

    def momsTouch(self, stroke):
        self.lang += stroke

if __name__ == '__main__':
    hum = Human()