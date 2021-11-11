"""
Módulo que comtem classe de validação e ajuste de dados
"""


class Validador:
    def valida(entrada, saida, valor_in):
        """
        Valida as informações de entrada e saida, e retorna a operacao a ser executada

        :param entrada, saida, valor_in: str
        :return: str, bool
        """
        if (entrada != saida) and Validador.teste_integridade(valor_in):
            return Validador.ajuste(entrada, saida)
        return False

    def teste_integridade(valor_in):
        """
        Testa o tipo do valor que foi digitado para evitar erro de tipo

        :param valor_in: str
        :return: bool
        """
        try:
            float(valor_in)
        except:
            return False
        return True

    def ajuste(entrada, saida):
        """
        Ajusta a entrada e saida em uma unica str usada para chamar a operacao de conversão
        
        :param entrada, saida: str
        :return: str
        """
        return f'{entrada}_{saida}'