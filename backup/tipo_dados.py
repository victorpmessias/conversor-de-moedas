from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction


class Conversor_dados:
    def altera_dados(self):
        _translate = QtCore.QCoreApplication.translate
        self.boxSaida.setItemText(1, _translate("MainWindow", "MB"))
        self.boxSaida.setItemText(2, _translate("MainWindow", "Mb"))
        self.boxSaida.setItemText(3, _translate("MainWindow", "KB"))
        self.boxSaida.setItemText(4, _translate("MainWindow", "Kb"))
        self.boxEntrada.setItemText(1, _translate("MainWindow", "MB"))
        self.boxEntrada.setItemText(2, _translate("MainWindow", "Mb"))
        self.boxEntrada.setItemText(3, _translate("MainWindow", "KB"))
        self.boxEntrada.setItemText(4, _translate("MainWindow", "Kb"))
