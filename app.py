"""
Módulo principal do conversor


"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from design import Ui_MainWindow
from conversor import Convert_dado, Convert_moeda


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
        Quando acianda esta função captura os dados e executa a operação de
        conversão

        :var entrada, saida, valor_in, resultado: str
        """
        entrada = self.boxEntrada.currentText()
        saida = self.boxSaida.currentText()
        valor_in = self.lineValorIn.text()
        if self.currentActive == 'dado':
            resultado = Convert_dado()
            resultado = resultado.calcular(entrada, saida, valor_in)
            self.lineResultado.setText(resultado)
        if self.currentActive == 'metrico':
            # TODO: implementar método de conversão métrico
            pass
        if self.currentActive == 'moeda':
            exec = Convert_moeda()
            resultado = exec.calcular(entrada,saida, valor_in)
            self.lineResultado.setText(resultado)

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    conversor = Conversor()
    conversor.show()
    qt.exec_()
