'''
5) Получить json словарь с сайта https://chainid.network/chains.json (с помощью requests) и вывести информацию о всех сетях в формате:
"name | первое rpc | есть ли поддержка EIP1559 | название нативной монеты | decimals нативной монеты | chain id | ссылка на експлорер"

6) Пользователь вводит chain_id и нужно вывести coin symbol (название нативной монеты в этой сети).
 Для получения информации использовать json словарь с сайта https://chainid.network/chains.json (с помощью requests)'''
# import requests
# url = 'https://chainid.network/chains.json'
# response = requests.get(url)
# data = response.json()
# # print(data)
#
# for elem in data:
#     name = elem['name']
#     nativeCurrency = elem['nativeCurrency']['symbol']
#     decimals = elem['nativeCurrency']['decimals']
#     chainid = elem['chainId']
#     if 'explorers' in elem and len(elem['explorers']) > 0 and 'url' in elem['explorers'][0] and len(
#             elem['explorers'][0]['url']) > 0:
#         explorer = elem['explorers'][0]['url']
#     if 'rpc' in elem and len(elem['rpc']) > 0:
#         rpc1 = elem['rpc'][0]
#     i = 0
#     if 'features' in elem:
#         for feature in elem['features']:
#             if feature.get('name') == 'EIP1559':
#                 eip1559 = 'eip1559 = yes'
#                 break
#             else:
#                 eip1559 = 'eip1559 = no'
#     print(name, rpc1, eip1559, nativeCurrency, decimals, chainid, explorer)

#
# import requests
# url = 'https://chainid.network/chains.json'
# response = requests.get(url)
# data = response.json()
# # print(data)
#
# int_chainid = int(input('vvedite chainid : '))
# for elem in data:
#     if 'chainId' in elem:
#         if elem['chainId'] == int_chainid:
#             nativeCurrency = elem['nativeCurrency']['symbol']
#             print(nativeCurrency)
#             break
