"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self):
        self.speed = ''
        self.name = ''
        self.is_police = False

    def go(self):
        return 'go'

    def stop(self):
        return 'stop'

    def turn(self, direction):
        return f'turn {direction}'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self):
        super().__init__()

    def show_speed(self):
        return 'превышение скорости' if self.speed > 60 else self.speed


class SportCar(Car):
    def __init__(self):
        super().__init__()


class WorkCar(Car):
    def __init__(self):
        super().__init__()

    def show_speed(self):
        return 'превышение скорости' if self.speed > 40 else self.speed


class PoliceCar(Car):
    def __init__(self):
        super().__init__()


town_car = TownCar()
town_car.name = 'tc'
town_car.is_police = False
town_car.speed = 30
print(town_car.go())
print(town_car.stop())
print(town_car.turn('left'))
print(town_car.show_speed())
town_car.speed = 61
print(town_car.name)
print(town_car.is_police)
print(town_car.show_speed())


sport_car = SportCar()
sport_car.name = 'sc'
sport_car.is_police = False
sport_car.speed = 30
print(sport_car.go())
print(sport_car.stop())
print(sport_car.turn('right'))
print(sport_car.show_speed())
sport_car.speed = 100
print(sport_car.name)
print(sport_car.is_police)
print(sport_car.show_speed())

work_car = WorkCar()
work_car.name = 'wc'
work_car.is_police = False
work_car.speed = 30
print(work_car.go())
print(work_car.stop())
print(work_car.turn('left'))
print(work_car.show_speed())
work_car.speed = 41
print(work_car.name)
print(work_car.is_police)
print(work_car.show_speed())

police_car = PoliceCar()
police_car.name = 'pc'
police_car.is_police = True
police_car.speed = 30
print(police_car.go())
print(police_car.stop())
print(police_car.turn('left'))
print(police_car.show_speed())
police_car.speed = 41
print(police_car.name)
print(police_car.is_police)
print(police_car.show_speed())


