# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


def profit():
    try:
        hour = int(input('Выработка в часах: '))
        money = int(input('Ставка, ₽: '))
        bonus = int(input('Премия, ₽: '))
        res = hour * money + bonus
        print(f'Заработная плата: {res} ₽')
    except ValueError:
        return print('Ошибка')


profit()
