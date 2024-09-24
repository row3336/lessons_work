#конкатенация или сложение строк (только строка + строка)
# s1 = 'hello'
# s2 = 'world'
# print(s1 + ', ' + s2 + '!!')  # hello, world!!

#сравнение строк по ASCII таблице https://www.asciitable.com/
# print(ord('A'), ord('a'))

# print('yes' > 'no') #сравнение по первым буквам False, если ASCII код одинаковый то сравниваются след символы
# print('qq' > 'q') #символ окончания строки \0 >> print('qq' > 'q\0')

# Примеры для практики
# print('abc' < 'ac')  # True
# print('abc' > 'ab')  # True
# print(420 > 5 and '420' > '5')  # False

# print('hello, \n \t \a world!!')

# тройные кавычки позволяют переносить строки
# экранирование
# s1 = 'He\'s said hi'
# print(s1)

#перенос инструкции или длинного условия

# A = int(input())
# B = int(input())
# C = int(input())
# M = int(input())
# K = int(input())
# if A < M and B < K or A < M and C < K or B < M and A < K or B < M and C < K or C < M and A < K or C < M and B < K:
# 	print('проходит')
# else:
# 	print('не проходит')

# A = int(input())
# B = int(input())
# C = int(input())
# M = int(input())
# K = int(input())
# if A < M and B < K or \
# 		A < M and C < K or \
# 		B < M and A < K or \
# 		B < M and C < K or \
# 		C < M and A < K or \
# 		C < M and B < K:
# 	print('проходит')
# else:
# 	print('не проходит')

#индексы в строке и срезы
# s = 'qwerty'
# print(s[0])  # q
# print(s[1])  # w
# print(s[2])  # e
# print(s[3])  # r
# print(s[4])  # t
# print(s[5])  # y
# print(s[6])  # string index out of range
# print(s[-1])  # y
# print(s[-2])  # t
# print(s[-3])  # r

# синтаксис:
# str[start:stop:step]
# s = 'qwerty'
# print(s[1:3])  # we
# print(s[1:6:2])  # wry
# # если хотим сделать срез "от начала", то можно ничего не писать в start:
# print(s[:4])  # qwer
# # если хотим сделать срез "до конца", то можно ничего не писать в stop:
# print(s[3:])  # rty
# # сделаем срез от начала до конца с шагом 2
# print(s[::2])  # qet
# # можно использовать отрицательный шаг
# print(s[5:0:-2])  # yrw
# # можно вывести слова "с конца"
# print(s[::-1])  # ytrewq

#строки через циклы

# через цикл while:
# s = 'qwerty'
# i = 0
# while i < len(s):
# 	print(s[i])
# 	i += 1
# # выведет q w e r t y (в столбик)
#
# # через цикл for:
# s = 'qwerty'
# for ch in s:
# 	print(ch)
# выведет q w e r t y (в столбик)


#Методы строк основные
s = 'rtqwerty'
# S.find(str, [start],[end])
# print(s.find('we'))  #1 индекс первого вхождения, подстрока начинается с третьего индекса
# print(s.find('rt')) #3
# print(s.find('rt', 1))  #c какого элемента начать поиск
# S.index(str, [start],[end])
# print(s.index('ry')) # отличие в том что если не найдет вызывает ошибку
# S.replace(шаблон, замена[, maxcount])
# print(s.replace('r', 'S')) #замена символа

# S.split(символ) # разбиение по рахделителю
# print(s.split('t')) #['r', 'qwer', 'y']
# разбивка текста на список слов
# s1 = 'Hello world yes no can'
# lst = s1.split()
# print(lst)  # ['Hello', 'world', 'yes', 'no', 'can']

# S.isdigit()  #digit true oe false
# s1 = '245432523'
# print(s.isdigit(), s1.isdigit())  #False True

# S.isalpha() # alphabet false true
# print(s.isalpha(), s1.isalpha())  #True False

# S.upper()
# print(s.upper())  #RTQWERTY
# # S.lower()
# print(s.lower())  #rtqwerty

# S.startswith(str)
# print(s.startswith('qw')) #False проверка начинается ли строка с ...
#
# S.endswith(str) #аналонично только конец строки

# S.join(список) #сборка строки из списка с разделителем S
# lst = ['c', 'home', 'desktop', 'folder']
# print('/'.join(lst))  #c/home/desktop/folder

# ord(символ) # символ в аски
# chr(число) # код аски в символ
# for i in range(1, 500):
#     print(chr(i))

# S.strip([chars])
# удаление всех ненужных пробелов и непечатных символов слева и справа строки

# S.count(str, [start],[end])
# считает сколько симоволов и подстрок встречается в строке

# последовательность вызовов
# s = 'agTtcAGtc'
# s.upper().count('gt'.upper())  # 2
#
# Вызовы происходя последовательно, но то, что в скобках имеет приоритет.
#
# 1. `.upper()`
# 2. `'gt'.upper()` (так как находится в скобках метода `.count()`
# 3. `.count()`