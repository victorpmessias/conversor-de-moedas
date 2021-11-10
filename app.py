"""
Módulo principal do conversor


"""
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from design import Ui_MainWindow
from caulc import Calcula



class Conversor(QMainWindow, Ui_MainWindow, QMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnConvert.clicked.connect(self.convert)
        self.actionDados_de_arm.triggered.connect(self.altera_dados)
        self.actionMoeda.triggered.connect(self.altera_moedas)
        self.actionMetrico.triggered.connect(self.altera_metrico)

    def convert(self):
        if self.lineValorIn.text() != '':
            calc = Calcula()
            if self.boxEntrada.currentText() == 'MB':
                if self.boxSaida.currentText() == 'Mb':
                    r = calc.mbyte_to_mbit(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'KB':
                    r = calc.mbyte_to_kbyte(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'Kb':
                    r = calc.mbyte_to_kbit(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'MB':
                    self.lineResultado.setText(
                        'Tipo de saida igual ao de entrada.')
                    return TypeError('Tipo de saida igual ao de entrada.')

            if self.boxEntrada.currentText() == 'Mb':
                if self.boxSaida.currentText() == 'MB':
                    r = calc.mbit_to_mbyte(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'KB':
                    r = calc.mbit_to_kbyte(self.lineValorIn.text())
                    self.lineResultado.setText(r)
                elif self.boxSaida.currentText() == 'Kb':
                    r = calc.mbit_to_kbit(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'Mb':
                    self.lineResultado.setText(
                        'Tipo de saida igual ao de entrada.')
                    return TypeError('Tipo de saida igual ao de entrada.')

            if self.boxEntrada.currentText() == 'KB':
                if self.boxSaida.currentText() == 'Mb':
                    r = calc.kbyte_to_mbits(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'MB':
                    r = calc.kbyte_to_mbyte(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'Kb':
                    r = calc.kbyte_to_kbit(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'KB':
                    self.lineResultado.setText(
                        'Tipo de saida igual ao de entrada.')
                    return TypeError('Tipo de saida igual ao de entrada.')

            if self.boxEntrada.currentText() == 'Kb':
                if self.boxSaida.currentText() == 'Mb':
                    r = calc.kbit_to_mbit(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'KB':
                    r = calc.kbit_to_kbyte(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'MB':
                    r = calc.kbit_to_mbyte(self.lineValorIn.text())
                    self.lineResultado.setText(r)

                elif self.boxSaida.currentText() == 'Kb':
                    self.lineResultado.setText(
                        'Tipo de saida igual ao de entrada.')
                    return TypeError('Tipo de saida igual ao de entrada.')

        else:
            self.lineResultado.setText('Você precisa digitar um valor.')

    

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    conversor = Conversor()
    conversor.show()
    qt.exec_()
