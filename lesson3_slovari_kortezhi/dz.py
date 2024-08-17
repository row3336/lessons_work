'''
1 уровень:
1) Есть 2 словаря. Объединить их без помощи функции update

2) Есть словарь с числовыми значениями. Посчитать среднюю по значениям

3) Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами,
 а элементы второго — соответственно значениями нашего словаря.

4) Когда Антон прочитал «Войну и мир», ему стало интересно,
сколько слов и в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы,
которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
Программа должна считывать одну строку со стандартного ввода и
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
в формате "слово количество" (см. пример вывода).
Порядок вывода слов может быть произвольным, каждое уникальное слово  должно выводиться только один раз

5) Получить json словарь с сайта https://chainid.network/chains.json (с помощью requests) и вывести информацию о всех сетях в формате:
"name | первое rpc | есть ли поддержка EIP1559 | название нативной монеты | decimals нативной монеты | chain id | ссылка на експлорер"

6) Пользователь вводит chain_id и нужно вывести coin symbol (название нативной монеты в этой сети).
 Для получения информации использовать json словарь с сайта https://chainid.network/chains.json (с помощью requests)'''

# 1) Есть 2 словаря. Объединить их без помощи функции update
# 2) Есть словарь с числовыми значениями. Посчитать среднюю по значениям

# d1 = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
# }
# d2 = {
#     'four': 4,
#     'five': 5,
#     'six': 6,
# }
# for key, val in d2.items():
#     d1[key] = val
# print(d1) #объединение
# i = 0
# summ = 0
# for val in d1.values():
#     summ += int(val)
#     i += 1
# print(f'summ = {summ}, elements = {i}')
# print('average =', summ / i) # среднее по числовым значениям

#
# 3) Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом, чтобы элементы первого списка были ключами,
#  а элементы второго — соответственно значениями нашего словаря.
# lst1 = ["one", "two", "three", "four", "five", "six", "seven"]
# lst2 = ['1', '2', '3', '4', '5', '6', '7']
# d = {}
# i = 0
# for _ in lst1:
#     d[_] = lst2[i]
#     i += 1
# print(d)


#
# 4) Когда Антон прочитал «Войну и мир», ему стало интересно,
# сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы,
# которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и
# выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра)
# в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово  должно выводиться только один раз

# text = input('введите текст :')
# text = text.lower()
# text += ' '
# words_list = []
# d = {}
# word = ''
#
# #билдим список слов
# for symb in text:
#     if symb == '.' or symb == ',' or symb == '!' or symb == '?' or symb == '—' or symb == '«' or symb == '»' or symb == ';' or symb == ':' or symb == '(' or symb == ')':
#         continue
#     elif symb == ' ':
#         if word == '':
#             continue
#         words_list.append(word)
#         word = ''
#     else:
#         word += symb
# print(words_list)
#
# #билдим словарь с количеством вхождений
# for w in words_list:
#     if w in d:
#         d[w] += 1
#     else:
#         d[w] = 1
# print(d)
#
# #сортируем в порядке убывания, dict() для преобразования кортежей в ключ-значения
# sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
# print(sorted_d)