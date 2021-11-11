class Calcula:
    def calcular(operacao, valor_in):
        result = None
        if operacao == '2' or '12':
            result = (float(valor_in)) * 8
        
        if operacao == '15' or '5':
            result = (float(valor_in)) / 8
        
        if operacao == '13':
            result = (float(valor_in)) / 8000

        if operacao == '14' or '9':
            result = (float(valor_in)) / 1000
    
        if operacao == '10':
            result = (float(valor_in)) / 125

        if operacao == '7':
            result = (float(valor_in)) * 125

        if operacao == '3' or '8':
            result = (float(valor_in)) * 1000

        if operacao == '4':
            result = (float(valor_in)) * 8000

        # if operacao == '1' or '6' or '11' or '16':
        #     result = None

        return str(result)
