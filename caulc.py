"""
Módulo que contém a classe responsavel por executar as operações de conversão.
"""


class Calcula:
    def kbit_to_kbyte(self, valor_in):
        result = (float(valor_in)) / 8
        return result

    def kbit_to_mbyte(self, valor_in):
        result = (float(valor_in)) / 8
        return result

    def kbit_to_mbit(self, valor_in):
        result = (float(valor_in)) / 1000
        return result

    def kbyte_to_kbit(self, valor_in):
        result = (float(valor_in)) * 8
        return result

    def kbyte_to_mbyte(self, valor_in):
        result = (float(valor_in)) / 1000
        return result

    def kbyte_to_mbits(self, valor_in):
        result = (float(valor_in)) / 125
        return result

    def mbit_to_mbyte(self, valor_in):
        result = (float(valor_in)) / 8
        return result

    def mbit_to_kbyte(self, valor_in):
        result = (float(valor_in)) * 125
        return result

    def mbit_to_kbit(self, valor_in):
        result = (float(valor_in)) * 1000
        return result
        
    def mbyte_to_mbit(self, valor_in):
        result = (float(valor_in)) * 8
        return str(result)

    def mbyte_to_kbyte(self, valor_in):
        result = (float(valor_in)) * 1000
        return str(result)

    def mbyte_to_kbit(self, valor_in):
        result = (float(valor_in)) * 8000
        return str(result)
