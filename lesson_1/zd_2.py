# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input('Введите время в секундах: '))

hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60

print(f'Время: {hour:02d}:{minute:02d}:{second:02d}')
