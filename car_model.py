class Car:
    def __init__(self, speed):
        self.speed = speed

    def model(self):
        if self.speed <= 100:
            return "Ford"
        elif self.speed <= 170:
            return "Mahendhra Thar"
        else:
            return "BMW"
car=Car(30)
print(car.model())