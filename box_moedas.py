# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'box_moeda.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.boxEntrada_moedas = QtWidgets.QComboBox(Form)
        self.boxEntrada_moedas.setGeometry(QtCore.QRect(10, 100, 376, 20))
        self.boxEntrada_moedas.setObjectName("boxEntrada_moedas")
        self.boxEntrada_moedas.addItem("")
        self.boxEntrada_moedas.addItem("")
        self.boxEntrada_moedas.addItem("")
        self.boxEntrada_moedas.addItem("")
        self.boxEntrada_moedas.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.boxEntrada_moedas.setItemText(0, _translate("Form", "Escolha o tipo de entrada"))
        self.boxEntrada_moedas.setItemText(1, _translate("Form", "R$"))
        self.boxEntrada_moedas.setItemText(2, _translate("Form", "ER"))
        self.boxEntrada_moedas.setItemText(3, _translate("Form", "$"))
        self.boxEntrada_moedas.setItemText(4, _translate("Form", "Libras"))
