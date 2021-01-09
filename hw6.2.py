#  2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса.
#  Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
#  необходимого для покрытия всего дорожного полотна.
#  Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    length = None
    width = None
    mass = None
    thickness = None

    def __init__(self, length, width, mass, thickness):
        self.length = length
        self.width = width
        self.mass = mass
        self.thickness = thickness

        print("В метод добавлены величины: длина - ", self.length, "ширина -", self.width, "масса -", self.mass, "толщина",
              self.thickness)


class Road_two(Road):
    def __init__(self, length, width, mass, thickness):
        super().__init__(length, width, mass, thickness)

    def asphalt_mass(self):
        asphalt_mass = self.length * self.width * self.width * self.mass
        print("Масса асфальта:", asphalt_mass, "тон.")


my_Road = Road_two(20, 50, 25, 5)
my_Road.asphalt_mass()
