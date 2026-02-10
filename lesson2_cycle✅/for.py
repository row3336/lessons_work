# for _ in range(1,6):   # range(start, stop, step)
#     print(_)

'''
- `start` – начало последовательности (**входит** в последовательность)
- `stop` – конец последовательности (**НЕ** **входит** в последовательность)
- `step` – шаг 
- В функцию `range` можно передать 1, 2 или 3 параметра:
- `range(stop)` – в этом случае по умолчанию `start=0` `step=1`
- `range(start, stop)` – в этом случае по умолчанию `step=1`
'''

# range(5) # 0, 1, 2, 3, 4
# range(3, 9) # 3, 4, 5, 6, 7, 8
# range(8, 20, 3) # 8, 11, 14, 17

# Списки
'''
list_name = [item1, item2, item3]
lst = [12, 'hello', [1, 2, 3], False, 99.87]
'''
#
# wallet_1 = '0xjkewjg8w78h298th29th92t'
# wallet_2 = '0xjkewjg8w78h298th29th92t'
# wallet_3 = '0xjkewjg8w78h298th29th92t'

# print(wallet_1)
# print(wallet_2)
# print(wallet_3)

# for i in wallet_1, wallet_2, wallet_3:
#     print(i)

# >>>
# wallets = ['0xjkewjg8w78h298th29th92t',
#            '0xjkewjg8w78h29832ewfs653',
#            '0xjkewjg8w78h2sdfsefee32t',
#            ]
# for i in wallets:
#     print(i)

# print(list(range(0,5))) #перобразование ренжа в список
#
# lst = [88, 'hi', True, 57, 9] #обращение к элементу списка
# print(lst[1])
#
# a = 'hello'
# print(a[1]) #обращение к эелементу строки

# lst = [88, 'hi', True, 57, 9]
# print(lst[0:3]) #срез
#
# lst = [12, 5, 76, 123, 8, 98, 3, 65]
# print(len(lst)) # получаем длинну списка
#
# lst.append(999999) #добавление элемента списка в конец
# print(lst)
#
# del(lst[0]) # удаление первого элемента списка
# print(lst)
#
# if 98 in  lst:
#     lst.remove(98) # удаление элемента по знаению
# else:
#     print('элемент не в списке')
# print(lst)
#
# print(lst.index(3)) # получение индекса элемента первого с таким значение в списке

# lst = [12, 5, 76, 123, 8, 98, 3, 65]
# for i in lst:
#     print(i)
#
# lst = [12, 5, 76, 123, 8, 98, 3, 65]
# i = 0
# while i < len(lst):
#     print(lst[i])
#     i += 1
