class Conversor_metrico:
      def altera_metrico(self):
        translate = QtCore.QCoreApplication.translate
        # Alteração das informações de entrada
        self.boxSaida.setItemText(1, _translate("MainWindow", "KM"))
        self.boxSaida.setItemText(2, _translate("MainWindow", "Jardas"))
        self.boxSaida.setItemText(3, _translate("MainWindow", "Polegadas"))
        self.boxSaida.setItemText(4, _translate("MainWindow", "Pés"))
        # Alteração das informações de entrada
        self.boxEntrada.setItemText(1, _translate("MainWindow", "KM"))
        self.boxEntrada.setItemText(2, _translate("MainWindow", "Jardas"))
        self.boxEntrada.setItemText(3, _translate("MainWindow", "Polegadas"))
        self.boxEntrada.setItemText(4, _translate("MainWindow", "Pés"))