# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


my_f = open('text3.txt', 'r', encoding='utf-8')
my_lst = my_f.read().split('\n')
pro = []
bad = []

for el in my_lst:
    el = el.split()
    if int(el[1]) < 20000:
        bad.append(el[0])
    pro.append(el[1])

print(f'Оклад менее 20000.0 ₽: {bad}\nСредний оклад: {sum(map(int, pro)) / len(pro)}'' ₽')

my_f.close()