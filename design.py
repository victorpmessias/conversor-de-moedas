# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon.fromTheme("C:\\Python\\Curso_Python\\PYQT_Aulas\\imgs\\outline_calculate_black_24dp.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #494C51;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #353A40;")
        self.centralwidget.setObjectName("centralwidget")
        self.boxSaida = QtWidgets.QComboBox(self.centralwidget)
        self.boxSaida.setGeometry(QtCore.QRect(10, 40, 281, 18))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.boxSaida.setFont(font)
        self.boxSaida.setStyleSheet("background-color: white;")
        self.boxSaida.setObjectName("boxSaida")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.lineValorIn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineValorIn.setGeometry(QtCore.QRect(10, 80, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.lineValorIn.setFont(font)
        self.lineValorIn.setStyleSheet("background-color: white;")
        self.lineValorIn.setText("")
        self.lineValorIn.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineValorIn.setObjectName("lineValorIn")
        self.btnConvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(210, 80, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(8)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btnConvert.setFont(font)
        self.btnConvert.setStyleSheet("background-color: #0083F9; color: white")
        self.btnConvert.setObjectName("btnConvert")
        self.boxEntrada = QtWidgets.QComboBox(self.centralwidget)
        self.boxEntrada.setGeometry(QtCore.QRect(10, 10, 281, 18))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.boxEntrada.setFont(font)
        self.boxEntrada.setStyleSheet("background-color: white; color: red;")
        self.boxEntrada.setObjectName("boxEntrada")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.lineResultado = QtWidgets.QLineEdit(self.centralwidget)
        self.lineResultado.setGeometry(QtCore.QRect(9, 118, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.lineResultado.setFont(font)
        self.lineResultado.setStyleSheet("background-color: white;")
        self.lineResultado.setText("")
        self.lineResultado.setReadOnly(True)
        self.lineResultado.setObjectName("lineResultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setStyleSheet("background-color: #494C51; color: white;")
        self.menubar.setObjectName("menubar")
        self.menuTipo_de_dado = QtWidgets.QMenu(self.menubar)
        self.menuTipo_de_dado.setStyleSheet("background-color: gray; color: white;")
        self.menuTipo_de_dado.setObjectName("menuTipo_de_dado")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDados_de_arm = QtWidgets.QAction(MainWindow)
        self.actionDados_de_arm.setObjectName("actionDados_de_arm")
        self.actionMoeda = QtWidgets.QAction(MainWindow)
        self.actionMoeda.setObjectName("actionMoeda")
        self.actionMetrico = QtWidgets.QAction(MainWindow)
        self.actionMetrico.setObjectName("actionMetrico")
        self.menuTipo_de_dado.addAction(self.actionDados_de_arm)
        self.menuTipo_de_dado.addAction(self.actionMoeda)
        self.menuTipo_de_dado.addAction(self.actionMetrico)
        self.menubar.addAction(self.menuTipo_de_dado.menuAction())
        self.currentActive = 'dado'
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conversor de medidas"))
        self.boxSaida.setItemText(0, _translate("MainWindow", "Escolha o tipo de saida"))
        self.boxSaida.setItemText(1, _translate("MainWindow", "MB"))
        self.boxSaida.setItemText(2, _translate("MainWindow", "Mb"))
        self.boxSaida.setItemText(3, _translate("MainWindow", "KB"))
        self.boxSaida.setItemText(4, _translate("MainWindow", "Kb"))
        self.lineValorIn.setPlaceholderText(_translate("MainWindow", "Insira um valor"))
        self.btnConvert.setText(_translate("MainWindow", "CONVERTER"))
        self.boxEntrada.setItemText(0, _translate("MainWindow", "Escolha o tipo de entrada"))
        self.boxEntrada.setItemText(1, _translate("MainWindow", "MB"))
        self.boxEntrada.setItemText(2, _translate("MainWindow", "Mb"))
        self.boxEntrada.setItemText(3, _translate("MainWindow", "KB"))
        self.boxEntrada.setItemText(4, _translate("MainWindow", "Kb"))
        self.lineResultado.setPlaceholderText(_translate("MainWindow", "Resultado"))
        self.menuTipo_de_dado.setTitle(_translate("MainWindow", "Tipo de dado"))
        self.actionDados_de_arm.setText(_translate("MainWindow", "Dados de arm."))
        self.actionMoeda.setText(_translate("MainWindow", "Moeda"))
        self.actionMetrico.setText(_translate("MainWindow", "Metrico"))

    def altera_dados(self):
        _translate = QtCore.QCoreApplication.translate
        # Alteração das informações de entrada
        self.boxEntrada.setItemText(1, _translate("MainWindow", "MB"))
        self.boxEntrada.setItemText(2, _translate("MainWindow", "Mb"))
        self.boxEntrada.setItemText(3, _translate("MainWindow", "KB"))
        self.boxEntrada.setItemText(4, _translate("MainWindow", "Kb"))
        # Alteração das informações de saida
        self.boxSaida.setItemText(1, _translate("MainWindow", "MB"))
        self.boxSaida.setItemText(2, _translate("MainWindow", "Mb"))
        self.boxSaida.setItemText(3, _translate("MainWindow", "KB"))
        self.boxSaida.setItemText(4, _translate("MainWindow", "Kb"))
        # Variavel de controle
        self.currentActive = 'dado'

    def altera_moedas(self):
        _translate = QtCore.QCoreApplication.translate
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
        # Variavel de controle
        self.currentActive = 'moeda'

    def altera_metrico(self):
        _translate = QtCore.QCoreApplication.translate
        # Alteração das informações de entrada
        self.boxSaida.setItemText(1, _translate("MainWindow", "KM"))
        self.boxSaida.setItemText(2, _translate("MainWindow", "Jardas"))
        self.boxSaida.setItemText(3, _translate("MainWindow", "Polegadas"))
        self.boxSaida.setItemText(4, _translate("MainWindow", "Pes"))
        # Alteração das informações de entrada
        self.boxEntrada.setItemText(1, _translate("MainWindow", "KM"))
        self.boxEntrada.setItemText(2, _translate("MainWindow", "Jardas"))
        self.boxEntrada.setItemText(3, _translate("MainWindow", "Polegadas"))
        self.boxEntrada.setItemText(4, _translate("MainWindow", "Pes"))
        # Variavel de controle
        self.currentActive = 'metrico'