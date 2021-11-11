"""
Api responsavel por coletar a cotação de moedas
"""

import json
import requests
import re


class Cotacao:
    def get_cotacao(self, operacao):
        oper_ajuste = re.sub('[_]', '-', operacao)
        get = re.sub('[-]', '', oper_ajuste)
        requisicao = requests.get(f'https://economia.awesomeapi.com.br/last/{oper_ajuste}/')
        cotacao = requisicao.json()
        result = float(cotacao[f'{get}']['ask'])
        return result



