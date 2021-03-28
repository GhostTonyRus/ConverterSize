# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressbar_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoardingScreen(object):
    def setupUi(self, LoardingScreen):
        LoardingScreen.setObjectName("LoardingScreen")
        LoardingScreen.resize(700, 400)
        LoardingScreen.setMinimumSize(QtCore.QSize(700, 400))
        LoardingScreen.setMaximumSize(QtCore.QSize(700, 400))
        self.centralwidget = QtWidgets.QWidget(LoardingScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 701, 401))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: #222831;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_title = QtWidgets.QLabel(self.frame)
        self.lbl_title.setGeometry(QtCore.QRect(10, 110, 681, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: #ffd369;")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.lbl_description = QtWidgets.QLabel(self.frame)
        self.lbl_description.setGeometry(QtCore.QRect(10, 170, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_description.setFont(font)
        self.lbl_description.setStyleSheet("color: rgb(98, 114, 164);")
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(50, 230, 601, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(98, 114, 164);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radious: 10px;\n"
"    background-color:  #ffd369;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lbl_version = QtWidgets.QLabel(self.frame)
        self.lbl_version.setGeometry(QtCore.QRect(630, 360, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lbl_version.setFont(font)
        self.lbl_version.setStyleSheet("color: rgb(98, 114, 164);")
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_description_2 = QtWidgets.QLabel(self.frame)
        self.lbl_description_2.setGeometry(QtCore.QRect(10, 280, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_description_2.setFont(font)
        self.lbl_description_2.setStyleSheet("color: rgb(98, 114, 164);")
        self.lbl_description_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description_2.setObjectName("lbl_description_2")
        LoardingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoardingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoardingScreen)

    def retranslateUi(self, LoardingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoardingScreen.setWindowTitle(_translate("LoardingScreen", "MainWindow"))
        self.lbl_title.setText(_translate("LoardingScreen", "Инженерный калькулятор"))
        self.lbl_description.setText(_translate("LoardingScreen", "Калькулятор конвертер единиц"))
        self.lbl_version.setText(_translate("LoardingScreen", "v.2.1.0"))
        self.lbl_description_2.setText(_translate("LoardingScreen", "Загрузка..."))
