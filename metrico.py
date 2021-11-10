class Conversor_metrico:
      def altera_metrico(self):
        translate = QtCore.QCoreApplication.translate
        # Alteração das informações de entrada
        self.boxSaida.setItemText(1, _translate("MainWindow", "BRL"))
        self.boxSaida.setItemText(2, _translate("MainWindow", "USD"))
        self.boxSaida.setItemText(3, _translate("MainWindow", "JPY"))
        self.boxSaida.setItemText(4, _translate("MainWindow", "EUR"))
        # Alteração das informações de entrada
        self.boxEntrada.setItemText(1, _translate("MainWindow", "BRL"))
        self.boxEntrada.setItemText(2, _translate("MainWindow", "USD"))
        self.boxEntrada.setItemText(3, _translate("MainWindow", "JPY"))
        self.boxEntrada.setItemText(4, _translate("MainWindow", "EUR"))