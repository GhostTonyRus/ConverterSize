# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/exit_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exit_window_ui(object):
    def setupUi(self, Exit_window_ui):
        Exit_window_ui.setObjectName("Exit_window_ui")
        Exit_window_ui.resize(700, 400)
        Exit_window_ui.setMinimumSize(QtCore.QSize(700, 400))
        Exit_window_ui.setStyleSheet("QFrame{\n"
"    background-color: #222831;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Exit_window_ui)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 701, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbl_header = QtWidgets.QLabel(self.frame)
        self.lbl_header.setGeometry(QtCore.QRect(10, 70, 681, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        self.lbl_header.setFont(font)
        self.lbl_header.setStyleSheet("color: #ffd369;")
        self.lbl_header.setObjectName("lbl_header")
        self.btn_yes = QtWidgets.QPushButton(self.frame)
        self.btn_yes.setGeometry(QtCore.QRect(130, 170, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.btn_yes.setFont(font)
        self.btn_yes.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_yes.setStyleSheet("background-color: #393e46;\n"
"color: #ffd369;")
        self.btn_yes.setObjectName("btn_yes")
        self.btn_no = QtWidgets.QPushButton(self.frame)
        self.btn_no.setGeometry(QtCore.QRect(410, 170, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.btn_no.setFont(font)
        self.btn_no.setStyleSheet("background-color: #393e46;\n"
"color: #ffd369;")
        self.btn_no.setObjectName("btn_no")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(50, 280, 601, 23))
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
        self.lbl_description = QtWidgets.QLabel(self.frame)
        self.lbl_description.setGeometry(QtCore.QRect(10, 330, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_description.setFont(font)
        self.lbl_description.setStyleSheet("color: rgb(98, 114, 164);")
        self.lbl_description.setText("")
        self.lbl_description.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, -5, 671, 35))
        self.label.setStyleSheet("background-color: #393e46;\n"
"color: #ffd369;")
        self.label.setObjectName("label")
        self.lbl_icon = QtWidgets.QLabel(self.frame)
        self.lbl_icon.setGeometry(QtCore.QRect(0, 0, 30, 30))
        self.lbl_icon.setObjectName("lbl_icon")
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
        Exit_window_ui.setCentralWidget(self.centralwidget)

        self.retranslateUi(Exit_window_ui)
        QtCore.QMetaObject.connectSlotsByName(Exit_window_ui)

    def retranslateUi(self, Exit_window_ui):
        _translate = QtCore.QCoreApplication.translate
        Exit_window_ui.setWindowTitle(_translate("Exit_window_ui", "MainWindow"))
        self.lbl_header.setText(_translate("Exit_window_ui", "Вы действительно хотите бросить меня?"))
        self.btn_yes.setText(_translate("Exit_window_ui", "ДА"))
        self.btn_no.setText(_translate("Exit_window_ui", "НЕТ"))
        self.label.setText(_translate("Exit_window_ui", "    ИНЖЕНЕРНЫЙ ПЕРЕВОДЧИК"))
        self.lbl_icon.setText(_translate("Exit_window_ui", "TextLabel"))
        self.btn_close.setText(_translate("Exit_window_ui", "X"))
        self.btn_roll_up.setText(_translate("Exit_window_ui", "-"))