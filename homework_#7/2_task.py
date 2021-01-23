"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractproperty


class Clothes(ABC):
    @abstractproperty
    def consumption(self, size=0, height=0):
        """Расход ткани"""


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def consumption(self):
        return round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто - {self.consumption()}'


class Jacket(Clothes):
    def __init__(self, height):
        self.height = height

    def consumption(self):
        return round(self.height / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на на костюм - {self.consumption()}'


coat = Coat(100)
jacket = Jacket(200)
print(coat)
print(jacket)
print(coat.consumption() + jacket.consumption())
