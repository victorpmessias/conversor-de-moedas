"""
Módulo principal do conversor


"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from design import Ui_MainWindow
from conversor import Calcula


class Conversor(QMainWindow, Ui_MainWindow, QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnConvert.clicked.connect(self.incia)
        self.actionDados_de_arm.triggered.connect(self.altera_dados)
        self.actionMoeda.triggered.connect(self.altera_moedas)
        self.actionMetrico.triggered.connect(self.altera_metrico)

    def incia(self):
        self.convert()

    def convert(self):
        entrada = self.boxEntrada.currentText()
        saida = self.boxSaida.currentText()
        valor_in = self.lineValorIn.text()
        resultado = Calcula.calcular(entrada, saida, valor_in)
        self.lineResultado.setText(resultado)
        
      
        

        # valor_in = self.lineValorIn.text()
        # valida = Validador()
        # teste = valida.valida(valor_in)

        # if teste:
        #     box_in = self.boxEntrada.currentText()
        #     box_out = self.boxSaida.currentText()
        #     calc = Calcula()
        #     tipo = valida.tipo(box_in, box_out)
        #     resultado = calc.calcular(tipo, valor_in)
        #     self.lineResultado.setText(resultado)


        # else:
        #     self.lineResultado.setText('Você precisa digitar um valor.')

    

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    conversor = Conversor()
    conversor.show()
    qt.exec_()
