class car:
    def __init__(self):
        self.speed = 10

    def accel(self):
        self.speed += 10

    def __str__(self):
        return "속도"+str(self.speed)
