import json
import requests


requisicao = requests.get(" https://economia.awesomeapi.com.br/last/USD-JPY")
cotacao = requisicao.json()
print(cotacao['USDJPY']['code'])
result = float(cotacao['USDJPY']['ask'])

print(48.9*result)