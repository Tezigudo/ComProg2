'''get crypto price'''
import requests
import sys
import inspect
import re
import json


def get_crypto_price(crypto):
    '''get crypto price'''
    url = 'https://api.coinmarketcap.com/v1/ticker/{}'.format(crypto)
    response = requests.get(url)
    response_json = response.json()
    return response_json[0]['price_usd']

print(get_crypto_price('bitcoin'))
