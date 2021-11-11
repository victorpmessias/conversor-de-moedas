class Validador:
    def valida(self, valor):
        if valor != '':
            return True

    def tipo(self, valor_in, valor_out):
        r = 1
        if valor_in == 'MB':
            if valor_out == 'Mb':
                r += 2
                return r
            elif valor_out == 'KB': 
                r += 3
                return r 
            elif valor_out == 'Kb':
                r += 4
                return r
            elif valor_out == 'MB':
                r += 1
                return r

        if valor_in == 'Mb':
            if valor_out == 'MB':
                r += 5
                return r
            elif valor_out == 'KB':
                r += 6
                return r
            elif valor_out == 'Kb':
                r += 7
                return r
            elif valor_out == 'Mb':
                r += 8
                return r

        if valor_in == 'KB':
            if valor_out == 'Mb':
                r += 16
                return r
            elif valor_out == 'MB':
                r += 9
                return r
            elif valor_out == 'Kb':
                r += 10
                return r
            elif valor_out == 'KB':
                r += 11
                return r

        if valor_in == 'Kb':
            if valor_out == 'Mb':
                r += 12
                return r
            elif valor_out == 'KB':
                r += 13
                return r
            elif valor_out == 'MB':
                r += 14
                return r
            elif valor_out == 'Kb':
                r += 15
                return r

        return r



