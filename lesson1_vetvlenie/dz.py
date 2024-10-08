'''
Практика

1 уровень:
1) Пользователь вводит число a и число b. Возвести а в степень b
2) Пользователь вводит число от 1 до 7. Вывести соответствующий день недели
3) Пользователь вводит 2 числа. Вывести наибольшее из них
4) Пользователь вводит свой депозит и хороший курс доллара. Вывести в консоль депо в рублях и заплакать

2 уровень:
1) Пользователь вводит число. Если оно четное, вывести "четное". Если оно нечетное, вывести "нечетное"
2) Пользователь вводит 3 числа. Вывести наименьшее из них
3) Из нарнийского чата Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки. Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”. Получаемое число A всегда меньше либо равно B (то есть это проверять не надо).

3 уровень:
1) Написать простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введенным числам (“первое число” “операция” “второе число”) и выводит результат на экран.
Поддерживаемые операции: +, -, /, *, mod, pow, div, где:
mod - это взятие остатка от деления,
pow - возведение в степень,
div - целочисленное деление.
2) даны 2 числа a и b. Определить, делится ли a на b нацело. Делится ли b на a?
3) дано трёхзначное число. Определить, есть ли среди его цифр одинаковые
'''

# 1) Пользователь вводит число a и число b. Возвести а в степень b
# a = int(input('число1:'))
# b = int(input('число2:'))
# print('a**b=', a ** b)

# 2) Пользователь вводит число от 1 до 7. Вывести соответствующий день недели
# day = int(input('введите число от 1 до 7:'))
# if day == 1:
#     print('понедельник')
# elif day == 2:
#     print('вторник')
# elif day == 3:
#     print('среда')
# elif day == 4:
#     print('четверг')
# elif day == 5:
#     print('пятница')
# elif day == 6:
#     print('суббота')
# elif day == 7:
#     print('воскресенье')
# else:
#     print('out of range')

# 3) Пользователь вводит 2 числа. Вывести наибольшее из них
# a1 = int(input('1:'))
# a2 = int(input('2:'))
# if a1 > a2:
#     print(a1)
# elif a1 == a2:
#     print('числа равны')
# else:
#     print(a2)

# 4) Пользователь вводит свой депозит и хороший курс доллара. Вывести в консоль депо в рублях и заплакать
# dep = int(input('deposit USD:'))
# ex_rate = int(input('exchange rate:'))
# print('your deposit * exchange rate = ', dep * ex_rate)

# # 1) Пользователь вводит число. Если оно четное, вывести "четное". Если оно нечетное, вывести "нечетное"
# a1 = int(input('введите число: '))
# if (a1 % 2) == 1:
#     print('нечетное')
# else:
#     print('четное')

# 2) Пользователь вводит 3 числа. Вывести наименьшее из них
# a1 = int(input('число1: '))
# a2 = int(input('число2: '))
# a3 = int(input('число3: '))
# if a1 <= a2 and a1 <= a3:
#     print(f'наименьшее число {a1}')
# elif a2 <= a1 and a2 <= a3:
#     print(f'наименьшее число {a2}')
# if a3 <= a2 and a3 <= a1:
#     print(f'наименьшее число {a3}')

# 3) Из нарнийского чата Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать тоже вредно
# и не стоит спать более B часов. Сейчас Аня спит H часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям Сергея, выведите “Это нормально”.
# Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
# Получаемое число A всегда меньше либо равно B (то есть это проверять не надо).
# r_min = int(input('рекомендуется спать мин: '))
# r_max = int(input('рекомендуется спать макс: '))
# a_sleep = int(input('Анна спит: '))
# if a_sleep >= r_min and a_sleep <= r_max:
#     print('это нормально')
# elif a_sleep < r_min:
#     print('недосып')
# elif a_sleep > r_max:
#     print('пересып')


# LEVEL 3
# 1) Написать простой калькулятор, который считывает с пользовательского ввода три строки:
# первое число, второе число и операцию, после чего применяет операцию к введенным числам
# (“первое число” “операция” “второе число”) и выводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где:
# mod - это взятие остатка от деления,
# pow - возведение в степень,
# div - целочисленное деление.
# a1 = int(input('число1: '))
# a2 = int(input('число2: '))
# f = input('введите операцию: ')
# if f == '+':
#     print(f'{a1} + {a2} = ', a1 + a2)
# elif f == '-':
#     print(f'{a1} - {a2} = ', a1 - a2)
# elif f == '*':
#     print(f'{a1} * {a2} = ', a1 * a2)
# elif f == '/':
#     print(f'{a1} / {a2} =', a1 / a2)
# elif f == 'mod':
#     print(f'{a1} % {a2} = ', a1 % a2)
# elif f == 'pow':
#     print(f'{a1} ** {a2} = ', a1 ** a2)
# elif f == 'div':
#     print(f'{a1} // {a2} = ', a1 // a2)

# 2) даны 2 числа a и b. Определить, делится ли a на b нацело. Делится ли b на a?
# a1 = int(input('число1: '))
# a2 = int(input('число2: '))
# if a1 % a2 == 0:
#     print('a1 делится нацело a2')
# else:
#     print('число а1 не делится нацело на а2')
# if a2 % a1 == 0:
#     print('a2 делится нацело a1')
# else:
#     print('число а2 не делится нацело на а1')


# 3) дано трёхзначное число. Определить, есть ли среди его цифр одинаковые
# a = int(input('введите трехзначное число: '))
# a1 = a // 100
# a3 = a % 10
# a2_temp = a // 10
# a2 = a2_temp % 10
# # print(a1, a2, a3)
# if a1 == a2 or a1 == a3:
#     print('есть совпадения')
# else:
#     print('совпадений нету')