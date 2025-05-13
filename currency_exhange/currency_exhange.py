# mycoin = int(input('Please, enter the number of mycoins you have:>'))
# dollar_USA_exchange_rate = int(input('Please, enter the exchange rate:>'))
# ARS = 0.28
# HNL = 0.71
# AUD = 1.24
# MAD = 0.23
# exchange = mycoin*dollar_USA_exchange_rate
# print(f'The total amount of dollars: {exchange}')
# amounts = [
#    ['Total amount of ARS`s', mycoin*ARS],
#    ['Total amount of HNL`s', mycoin*HNL],
#    ['Total amount of AUD`s', mycoin*AUD],
#    ['Total amount of MAD`s', mycoin*MAD]
# ]
# for label, value in amounts:
#    print(f'{label}: {value:.2f}')
from json import JSONDecodeError
import requests

while True:
    base_currency = input('Enter your base currency:\n>').lower()
    url = f"http://www.floatrates.com/daily/{base_currency}.json"
    try:
        response = requests.get(url)
        rates = response.json()
        if not rates:
            print('Invalid currency!')
            continue
        break
    except JSONDecodeError:
        print('Invalid currency code')
cache = {}
for code in ['usd', 'eur']:
    if code in rates:
        cache[code] = rates[code]
while True:
    target_currency = input('Enter a target currency or press Enter to exit:\n>').lower()
    if not target_currency:
        break
    try:
        amount = float(input('Enter the amount of money you want to exсhange:'))
    except ValueError:
        print('Invalid amount. Please enter a number.')
        continue
    print('Checking a cache...')
    if target_currency in cache:
        print('Its in the cache')
        rate = cache[target_currency]['rate']
    else:
        print('Sorry, but it is not in cache')
        if target_currency in rates:
            cache[target_currency] = rates[target_currency]
            rate = rates[target_currency]['rate']
        else:
            print('Currency not found')
            continue
    exchanged = round(amount*rate, 2)
    print(f'You received {exchanged} {target_currency.upper()}')
