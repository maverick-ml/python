# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

nmb = int(input('Введите натуральное число: '))
lst = [7, 5, 3, 3, 2]
n = lst.count(nmb)

for el in lst:
    if n > 0:
        i = lst.index(nmb)
        lst.insert(i+n, nmb)
        break
    else:
        if nmb > el:
            j = lst.index(el)
            lst.insert(j, nmb)
            break
        elif nmb < lst[len(lst) - 1]:
            lst.append(nmb)
print(lst)
