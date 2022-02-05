"""
Módulo principal do conversor
"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu
from design import Ui_MainWindow
from conversor import ConvertDado, ConvertMoeda, ConvertMetrico


class Conversor(QMainWindow, Ui_MainWindow, QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnConvert.clicked.connect(self.convert)
        self.actionDados_de_arm.triggered.connect(self.altera_dados)
        self.actionMoeda.triggered.connect(self.altera_moedas)
        self.actionMetrico.triggered.connect(self.altera_metrico)

    def convert(self):
        """
        Quando acioanda esta função captura os dados e executa a operação de asiim
        conversão
        """
        entrada = self.boxEntrada.currentText()
        saida = self.boxSaida.currentText()
        valor_in = self.lineValorIn.text()
        if self.currentActive == 'dado':
            exec = ConvertDado()
            resultado = exec.calcular(entrada, saida, valor_in)
            self.lineResultado.setText(resultado)

        if self.currentActive == 'metrico':
            exec = ConvertMetrico()
            resultado = exec.calcular(entrada, saida, valor_in)
            self.lineResultado.setText(resultado)

        if self.currentActive == 'moeda':
            exec = ConvertMoeda()
            resultado = exec.calcular(entrada, saida, valor_in)
            self.lineResultado.setText(resultado)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    conversor = Conversor()
    conversor.show()
    qt.exec_()
