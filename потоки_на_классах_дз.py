import threading
from time import sleep

class Knight(threading.Thread):
    enemies = 100

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while Knight.enemies > 0:
            sleep(1)
            Knight.enemies -= self.power
            self.days += 1
            if Knight.enemies > 0:
                print(f"{self.name} сражается {self.days}..., осталось {Knight.enemies} воинов.")
            else:
                Knight.enemies = 0
                print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Битвы окончены")