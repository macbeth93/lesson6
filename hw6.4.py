#   Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color,
#   name, is_police (булево).
#   А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
#   повернула (куда).
#   Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
#   Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
#   Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
#   40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name + "Начала движение")

    def stop(self):
        print(self.name + "Остановилась")

    def turn(self, direction):
        print("Машина повернула на " + direction)

    def show_speed(self):
        print("Скорость:", self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.is_police = False
        if self.speed > 60:
            print("Виу-Виу! Вы превысили скорость!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.is_police = False


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.is_police = False
        if self.speed > 40:
            print("Виу-Виу! Вы превысили скорость!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.is_police = True


car_1 = TownCar(75, "red", "Bombeeta!", False)
