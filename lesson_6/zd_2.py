# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc(self):
        self.weigth = 25
        self.tick = 5
        calc = self.length * self.width * self.weigth * self.tick / 1000
        print(f'Необходимо: {calc} т')


Road = Road(5000, 20)
Road.calc()
