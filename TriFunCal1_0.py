# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TriFunCal1_0.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 372)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input = QtWidgets.QTextBrowser(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(59, 100, 421, 50))
        self.input.setMaximumSize(QtCore.QSize(16777215, 100))
        self.input.setObjectName("input")
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(60, 60, 421, 20))
        self.output.setObjectName("output")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 60, 54, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 54, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(59, 170, 421, 128))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_sin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_sin.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_sin.setMaximumSize(QtCore.QSize(60, 180))
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.gridLayout.addWidget(self.pushButton_sin, 0, 0, 1, 1)
        self.pushButton_cos = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_cos.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_cos.setMaximumSize(QtCore.QSize(60, 180))
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.gridLayout.addWidget(self.pushButton_cos, 0, 1, 1, 1)
        self.pushButton_ce = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ce.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_ce.setMaximumSize(QtCore.QSize(60, 180))
        self.pushButton_ce.setObjectName("pushButton_ce")
        self.gridLayout.addWidget(self.pushButton_ce, 0, 2, 1, 1)
        self.pushButton_arcsin = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_arcsin.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_arcsin.setMaximumSize(QtCore.QSize(60, 180))
        self.pushButton_arcsin.setObjectName("pushButton_arcsin")
        self.gridLayout.addWidget(self.pushButton_arcsin, 1, 0, 1, 1)
        self.pushButton_arctan = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_arctan.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_arctan.setMaximumSize(QtCore.QSize(60, 180))
        self.pushButton_arctan.setObjectName("pushButton_arctan")
        self.gridLayout.addWidget(self.pushButton_arctan, 1, 1, 1, 1)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(100, 60))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(60, 180))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout.addWidget(self.pushButton_clear, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 489, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  输入:"))
        self.label_2.setText(_translate("MainWindow", "  输出:"))
        self.pushButton_sin.setText(_translate("MainWindow", "sin"))
        self.pushButton_cos.setText(_translate("MainWindow", "cos"))
        self.pushButton_ce.setText(_translate("MainWindow", "ce"))
        self.pushButton_arcsin.setText(_translate("MainWindow", "arcsin"))
        self.pushButton_arctan.setText(_translate("MainWindow", "arctan"))
        self.pushButton_clear.setText(_translate("MainWindow", "clear"))