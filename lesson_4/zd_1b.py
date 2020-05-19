# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from sys import argv

num, hour, money, bonus = argv
try:
    hour = int(hour)
    money = int(money)
    bonus = int(bonus)
    res = hour * money + bonus
    print(f'Заработная плата: {res}')
except ValueError:
    print('Ошибка')