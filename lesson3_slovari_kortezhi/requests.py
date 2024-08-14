# import requests
# #pip install requests
# #pip3 install requests
#
# url = 'https://chainid.network/chains.json'
# response = requests.get(url)
# data = response.json()
#
# for elem in data:
#     decimals = elem['nattiveCurrency']['decimals']
#     if decimals != 18:
#         print(elem['name'], elem['nattiveCurrency']['symbol'], decimals)


# pair = input('введите торговую пару: ')
# pair = pair.upper()
# url = f'https://api.binance.com/api/v3/ticker/price?symbol={pair}'
# response = requests.get(url)
# data = response.json()
# if 'price' in data:
#     print(data['price'])
# else:
#     print('error')