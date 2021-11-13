# from urllib import request, parse
# import json

# url = 'https://neutrinoapi.net/convert'
# params = {
#   'user-id': 'victorpm',
#   'api-key': 'vM8ppe0OMRfuwcdZfsA8Ee9tbTIkS4RG8QkQOs0cnkGCYwXy',
#   'ip': '162.209.104.195',
#   'from-value': '1',
#   'from-type': 'yard',
#   'from-type': 'km',
# }

# postdata = parse.urlencode(params).encode()
# req = request.Request(url, data=postdata)
# response = request.urlopen(req)
# result = json.loads(response.read().decode("utf-8"))

# print(result)


class Metrico:
    @staticmethod
    def calcular(operacao: str, valor_in: str):
        if operacao == 'KM_Jardas':
            result = float(valor_in) * 1904
        if operacao == 'KM_Polegadas':
            result = float(valor_in) * 39370
        if operacao == 'KM_Pes':
            result = float(valor_in) * 3281

        if operacao == 'Jardas_KM':
            result = float(valor_in) / 1904
        if operacao == 'Jardas_Polegadas':
            result = float(valor_in) * 36
        if operacao == 'Jardas_Pes':
            result = float(valor_in) * 3

        if operacao == 'Pes_KM':
            result = float(valor_in) / 3281
        if operacao == 'Pes_Jardas':
            result = float(valor_in) / 3
        if operacao == 'Pes_Polegadas':
            result = float(valor_in) * 12

        if operacao == 'Polegdas_KM':
            result = float(valor_in) / 39370
        if operacao == 'Polegadas_Pes':
            result = float(valor_in) / 12
        if operacao == 'Polegadas_Jardas':
            result = float(valor_in) / 36

        return result
