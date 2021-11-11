"""
Módulo que contém a classe responsavel por executar as operações de conversão.
"""
from validador import Validador
from abc import ABC, abstractclassmethod
from api_cotacao import Cotacao


class Convert(ABC):
    def valida(self, entrada, saida, valor_in):
        operacao = Validador.valida(entrada, saida, valor_in)
        return operacao


    @abstractclassmethod
    def calcular(self, entrada, saida, valor_in):
        pass


class Convert_dado(Convert):
    def calcular(self, entrada, saida, valor_in):
        """
        Esta função inicia o processo de conversão, fazendo a chamada do
        validador,
        e retornando o resultado da operação

        :param entrada, saida, valor_in: str
        :return: str
        """
        operacao = self.valida(entrada, saida, valor_in)
        if operacao:
            if operacao == ('MB_Mb' or 'KB_Kb'):
                result = (float(valor_in)) * 8
                return str(result)

            if operacao == ('Kb_KB' or 'Mb_MB'):
                result = (float(valor_in)) / 8
                return str(result)

            if operacao == 'Kb_MB':
                result = (float(valor_in)) / 8000
                return str(result)

            if operacao == ('Kb_Mb' or 'KB_MB'):
                result = (float(valor_in)) / 1000
                return str(result)

            if operacao == 'KB_Mb':
                result = (float(valor_in)) / 125
                return str(result)

            if operacao == 'Mb_KB':
                result = (float(valor_in)) * 125
                return str(result)

            if operacao == ('MB_KB' or 'Mb_Kb'):
                result = (float(valor_in)) * 1000
                return str(result)

            if operacao == 'MB_Kb':
                result = (float(valor_in)) * 8000
                return str(result)

        return 'Operação Invalida'


class Convert_moeda(Convert):
    def calcular(self, entrada, saida, valor_in):
        """
        Esta função inicia o processo de conversão, fazendo a chamada do
        validador,
        e retornando o resultado da operação

        :param entrada, saida, valor_in: str
        :return: str
        """
        operacao = self.valida(entrada, saida, valor_in)
        if operacao:
            cotacao = Cotacao()
            cotacao_on = cotacao.get_cotacao(operacao)
            result = (float(valor_in)) * cotacao_on
            return str(result)
        return 'Operação Invalida'
