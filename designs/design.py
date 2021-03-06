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
        MainWindow.resize(310, 236)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon.fromTheme("C:\\Python\\Curso_Python\\PYQT_Aulas\\imgs\\outline_calculate_black_24dp.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #494C51;")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("background-color: #353A40;")
        self.centralwidget.setObjectName("centralwidget")
        self.boxSaida = QtWidgets.QComboBox(self.centralwidget)
        self.boxSaida.setGeometry(QtCore.QRect(10, 80, 281, 18))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.boxSaida.setFont(font)
        self.boxSaida.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boxSaida.setStyleSheet("background-color: white;")
        self.boxSaida.setObjectName("boxSaida")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.boxSaida.addItem("")
        self.lineValorIn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineValorIn.setGeometry(QtCore.QRect(10, 120, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.lineValorIn.setFont(font)
        self.lineValorIn.setStyleSheet("background-color: white;")
        self.lineValorIn.setText("")
        self.lineValorIn.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineValorIn.setObjectName("lineValorIn")
        self.btnConvert = QtWidgets.QPushButton(self.centralwidget)
        self.btnConvert.setGeometry(QtCore.QRect(210, 120, 81, 23))
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
        self.boxEntrada.setGeometry(QtCore.QRect(10, 40, 281, 18))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.boxEntrada.setFont(font)
        self.boxEntrada.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.boxEntrada.setStyleSheet("background-color: white; color: red;")
        self.boxEntrada.setObjectName("boxEntrada")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.boxEntrada.addItem("")
        self.lineResultado = QtWidgets.QLineEdit(self.centralwidget)
        self.lineResultado.setGeometry(QtCore.QRect(10, 160, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.lineResultado.setFont(font)
        self.lineResultado.setStyleSheet("background-color: white;")
        self.lineResultado.setText("")
        self.lineResultado.setReadOnly(True)
        self.lineResultado.setObjectName("lineResultado")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: #353A40; color: white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 310, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet("background-color: #494C51; color: white;")
        self.menubar.setObjectName("menubar")
        self.menuTipo_de_dado = QtWidgets.QMenu(self.menubar)
        self.menuTipo_de_dado.setStyleSheet("background-color: gray; color: white;")
        self.menuTipo_de_dado.setObjectName("menuTipo_de_dado")
        MainWindow.setMenuBar(self.menubar)
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
        self.label.setText(_translate("MainWindow", "CONVERTER DADOS"))
        self.menuTipo_de_dado.setTitle(_translate("MainWindow", "Tipo de dado"))
        self.actionDados_de_arm.setText(_translate("MainWindow", "Dados de arm."))
        self.actionMoeda.setText(_translate("MainWindow", "Moeda"))
        self.actionMetrico.setText(_translate("MainWindow", "Metrico"))
