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
        self.lbl_title.setGeometry(QtCore.QRect(10, 70, 681, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.lbl_title.setFont(font)
        self.lbl_title.setStyleSheet("color: #ffd369;")
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 140, 681, 251))
        self.stackedWidget.setStyleSheet("background-color: #222831;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.loarding_page = QtWidgets.QWidget()
        self.loarding_page.setObjectName("loarding_page")
        self.lbl_description_2 = QtWidgets.QLabel(self.loarding_page)
        self.lbl_description_2.setGeometry(QtCore.QRect(0, 140, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_description_2.setFont(font)
        self.lbl_description_2.setStyleSheet("color: rgb(98, 114, 164);")
        self.lbl_description_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description_2.setObjectName("lbl_description_2")
        self.lbl_version = QtWidgets.QLabel(self.loarding_page)
        self.lbl_version.setGeometry(QtCore.QRect(610, 220, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lbl_version.setFont(font)
        self.lbl_version.setStyleSheet("color: rgb(98, 114, 164);")
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.progressBar = QtWidgets.QProgressBar(self.loarding_page)
        self.progressBar.setGeometry(QtCore.QRect(40, 90, 601, 23))
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
        self.lbl_description = QtWidgets.QLabel(self.loarding_page)
        self.lbl_description.setGeometry(QtCore.QRect(0, 10, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_description.setFont(font)
        self.lbl_description.setStyleSheet("color: rgb(98, 114, 164);")
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.stackedWidget.addWidget(self.loarding_page)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.label = QtWidgets.QLabel(self.login_page)
        self.label.setGeometry(QtCore.QRect(110, 20, 481, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffd369;")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.le_password_input = QtWidgets.QLineEdit(self.login_page)
        self.le_password_input.setGeometry(QtCore.QRect(310, 140, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.le_password_input.setFont(font)
        self.le_password_input.setStyleSheet("QLineEdit {\n"
"        border-width: 3px;\n"
"        border-style: solid;\n"
"        border-color: #ffd369;    \n"
"        background-color: #393e46;\n"
"        color: #ffd369;\n"
" }\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"        border-color: rgb(255, 156, 0);\n"
" }\n"
"")
        self.le_password_input.setText("")
        self.le_password_input.setObjectName("le_password_input")
        self.label_2 = QtWidgets.QLabel(self.login_page)
        self.label_2.setGeometry(QtCore.QRect(130, 139, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #393e46;\n"
"color: #ffd369;\n"
"border-radius: 10px")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_login = QtWidgets.QPushButton(self.login_page)
        self.btn_login.setGeometry(QtCore.QRect(240, 200, 201, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet("background-color: #393e46;\n"
"color: #ffd369;")
        self.btn_login.setObjectName("btn_login")
        self.stackedWidget.addWidget(self.login_page)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, -5, 671, 35))
        self.label_3.setStyleSheet("background-color: #393e46;\n"
"color: #ffd369;")
        self.label_3.setObjectName("label_3")
        self.btn_roll_up = QtWidgets.QPushButton(self.frame)
        self.btn_roll_up.setGeometry(QtCore.QRect(630, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        self.btn_roll_up.setFont(font)
        self.btn_roll_up.setStyleSheet("color: #ffd369;\n"
"background-color: #222831;\n"
"")
        self.btn_roll_up.setObjectName("btn_roll_up")
        self.btn_close = QtWidgets.QPushButton(self.frame)
        self.btn_close.setGeometry(QtCore.QRect(670, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet("color: #ffd369;\n"
"background-color: #222831;\n"
"")
        self.btn_close.setObjectName("btn_close")
        self.lbl_icon = QtWidgets.QLabel(self.frame)
        self.lbl_icon.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.lbl_icon.setObjectName("lbl_icon")
        LoardingScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoardingScreen)
        QtCore.QMetaObject.connectSlotsByName(LoardingScreen)

    def retranslateUi(self, LoardingScreen):
        _translate = QtCore.QCoreApplication.translate
        LoardingScreen.setWindowTitle(_translate("LoardingScreen", "MainWindow"))
        self.lbl_title.setText(_translate("LoardingScreen", "Инженерный переводчик"))
        self.lbl_description_2.setText(_translate("LoardingScreen", "Загрузка..."))
        self.lbl_version.setText(_translate("LoardingScreen", "v.2.1.1"))
        self.lbl_description.setText(_translate("LoardingScreen", "Конвертер единиц и калькулятор"))
        self.label.setText(_translate("LoardingScreen", "Здравствуйте Вадим Дмитриевич введите пожалуйста пароль для использования сверхтехнологичной программы"))
        self.label_2.setText(_translate("LoardingScreen", "ПАРОЛЬ:"))
        self.btn_login.setText(_translate("LoardingScreen", "ВОЙТИ"))
        self.label_3.setText(_translate("LoardingScreen", "   ИНЖЕНЕРНЫЙ ПЕРЕВОДЧИК"))
        self.btn_roll_up.setText(_translate("LoardingScreen", "-"))
        self.btn_close.setText(_translate("LoardingScreen", "X"))
        self.lbl_icon.setText(_translate("LoardingScreen", "TextLabel"))
