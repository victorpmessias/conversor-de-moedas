from enum import Enum, auto


class Tipo_Operacao(Enum):
    MB_MB = auto()
    MB_Mb = auto()
    MB_KB = auto()
    MB_Kb = auto()
    Mb_MB = auto()
    Mb_Mb = auto()
    Mb_KB = auto()
    Mb_Kb = auto()
    KB_MB = auto()
    KB_Mb = auto()
    KB_KB = auto()
    KB_Kb = auto()
    Kb_MB = auto()
    Kb_Mb = auto()
    Kb_KB = auto()
    Kb_Kb = auto()


class Validador:
    def valida(valor1, valor2):
        return f'{valor1}_{valor2}'

    def teste(valor):
        tipodict = {}
        for i in Tipo_Operacao:
            # print(i, i.value)
            tipodict[i.name] = i.value
        if valor in tipodict:
            return tipodict[valor]
        else:
            return None


