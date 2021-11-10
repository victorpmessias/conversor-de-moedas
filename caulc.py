"""
Módulo que contém a classe responsavel por executar as operações de conversão.
"""


class Calcula:
    def calcular(self, operacao, valor_in):
        operacao = int(operacao)
        if operacao == 14 or 6:
            # kbit_to_kbyte(self, valor_in):
            result = (float(valor_in)) / 8
            return str(result)
        elif operacao == 15:
            # kbit_to_mbyte(self, valor_in):
            result = (float(valor_in)) / 8000
            return str(result)
        elif operacao == 13 or 9:
            # kbit_to_mbit(self, valor_in):
            result = (float(valor_in)) / 1000
            return str(result)
        elif operacao == 11 or 3:
            # kbyte_to_kbit(self, valor_in):
            result = (float(valor_in)) * 8
            return str(result)

            # # kbyte_to_mbyte(self, valor_in):
            # str(result) = (float(valor_in)) / 1000
            # return str(result)
        elif operacao == 17:
            print(operacao)
            # kbyte_to_mbits(self, valor_in):
            result = (float(valor_in)) / 125
            return str(result)

            # # mbit_to_mbyte(self, valor_in):
            # str(result) = (float(valor_in)) / 8
            # return str(result)
        elif operacao == 7:
            # mbit_to_kbyte(self, valor_in):
            result = (float(valor_in)) * 125
            return str(result)

        elif operacao == 8 or 4:
            # mbit_to_kbit(self, valor_in):
            result = (float(valor_in)) * 1000
            return str(result)
            
            # mbyte_to_mbit(self, valor_in):
            # str(result) = (float(valor_in)) * 8
            # return str(str(result))

            # mbyte_to_kbyte(self, valor_in):
            # str(result) = (float(valor_in)) * 1000
            # return str(str(result))

        elif operacao == 5:
            # mbyte_to_kbit(self, valor_in):
            result = (float(valor_in)) * 8000
            return str(result)

        elif operacao == 2:
            return None
        


