import requests
from typing import Union, Optional


# def say_hi():
#     print('hello')

# def my_summ(a, b)                                                # без анотаций типов

# def my_summ(a: int, b: int):                                     # аннотации типов !!!! а = число, в = число

# def my_summ(a: Union[int, float] b: Union[int, float]):          # анотации типов используя Union

# def my_summ(                                                       # лучший вариант подачи кода используя Union пайпы |
#         a: int | float,                                            # целое число или дробное числоб функция сама себя описывает
#         b: int | float
# ):
#     print(a + b)
#
#
# my_summ(5, 6)
# my_summ(a = int(input('vvedite 4islo a = ')), b = int(input('vvedite 4islo b = ')))
# my_summ(b=5, a=6)  #правильно подставлять значения через равно

# def my_summ(a = int(input('vvedite 4islo a = ')), b = int(input('vvedite 4islo b = '))):
#     print(a + b)
#
#
# my_summ


# def my_summ(
#         a: int | float,
#         b: int | float,
#         lst: list[int] #cюда прийдет список состоящий из целых чисел
# ):
#     print(a + b)


# def get_smallest_number(a: int | float, b: int | float):
#     if a < b:
#         print(a)
#     else:
#         print(b)
#
#
# get_smallest_number(3, 9)
# get_smallest_number(-4, 32.54)

#значения по умолчанию,указываются только в конце после анотаций типов

# def say_hi(name: str = 'noname'):
#     print(f'hello, {name}')
#
#
# say_hi()   # hello noname
# say_hi("Bob") # hello Bob
# say_hi('John')

# def say_hi(name: str | None = None):  # передается строка либо None, по умолчанию None
#   if name:
#       print(f'hello, {name}!!')
#   else:
#     print(f'hello!!')
#
#
# say_hi()   # hello noname
# say_hi("Bob") # hello Bob
# say_hi('John')



#пример передачи аргументов по значению
# def foo(a: int):
# 	a = 42
#
# a = 1  # не обязательно переменную называть a
# foo(a)
# print(a)  # 1
#
# #пример передачи аргументов по ссылке
# def foo(lst: list):
# 	lst[0] = 42
#
# my_lst = [1, 2, 3]
# foo(lst=my_lst)
# print(my_lst)  # [42, 2, 3]

# return - позволяет вернуть что то из функции не используя глобальные переменные


# def foo(a : int):
#     a = 42
#     result = a * 2
#     return result    # то что написано после return будет подставлено на место функции! ! ! сразу выход из функции, else можно не писать
#
#
# q = 5
# q = foo(a=q)
# print(q)   # 84


# def get_smallest_number(a: int | float, b: int | float) -> int | float:  # сокращение с помощью return
#     if a < b:
#         return a
#     return b
#
#
# get_smallest_number(3, 9)
# get_smallest_number(-4, 32.54)