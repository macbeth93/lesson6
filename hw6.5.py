# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки предметом:", self.title)


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def start(self):
        print("Отрисовка Ручкой")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def start(self):
        print("Отрисовка карандашом")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def start(self):
        print("Отрисовка маркером")


my_pen = Pen("Ручка")
my_pen.draw()
my_pen.start()
