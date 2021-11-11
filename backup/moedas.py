from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction


class Altera_btn:
    def altera_moedas(self):
        _translate = QtCore.QCoreApplication.translate
        # Alteração das informações de entrada
        self.boxEntrada.setItemText(0, _translate(
            "MainWindow", "Escolha o tipo de entrada"))
        self.boxEntrada.setItemText(1, _translate("MainWindow", "R$"))
        self.boxEntrada.setItemText(2, _translate("MainWindow", "ER"))
        self.boxEntrada.setItemText(3, _translate("MainWindow", "$"))
        self.boxEntrada.setItemText(4, _translate("MainWindow", "Libras"))
        # Alteração das informações de saida
        self.boxSaida.setItemText(0, _translate(
            "MainWindow", "Escolha o tipo de saida"))
        self.boxSaida.setItemText(1, _translate("MainWindow", "R$"))
        self.boxSaida.setItemText(2, _translate("MainWindow", "ER"))
        self.boxSaida.setItemText(3, _translate("MainWindow", "$"))
        self.boxSaida.setItemText(4, _translate("MainWindow", "Libras"))
