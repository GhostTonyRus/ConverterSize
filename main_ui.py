# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1400, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1400, 900))
        MainWindow.setStyleSheet("background-color: black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1400, 900))
        self.centralwidget.setMaximumSize(QtCore.QSize(1400, 900))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 181, 881))
        self.listWidget.setObjectName("listWidget")
        self.btn_unit_converter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_unit_converter.setGeometry(QtCore.QRect(31, 59, 135, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.btn_unit_converter.setFont(font)
        self.btn_unit_converter.setStyleSheet("background-color: white")
        self.btn_unit_converter.setObjectName("btn_unit_converter")
        self.btn_calculator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculator.setGeometry(QtCore.QRect(30, 210, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.btn_calculator.setFont(font)
        self.btn_calculator.setStyleSheet("background-color: white")
        self.btn_calculator.setObjectName("btn_calculator")
        self.btn_ratio_converter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ratio_converter.setGeometry(QtCore.QRect(31, 132, 133, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.btn_ratio_converter.setFont(font)
        self.btn_ratio_converter.setStyleSheet("background-color: white")
        self.btn_ratio_converter.setObjectName("btn_ratio_converter")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(199, -1, 1190, 891))
        self.stackedWidget.setObjectName("stackedWidget")
        self.instruction = QtWidgets.QWidget()
        self.instruction.setObjectName("instruction")
        self.lbl_header = QtWidgets.QLabel(self.instruction)
        self.lbl_header.setGeometry(QtCore.QRect(370, 60, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_header.setFont(font)
        self.lbl_header.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbl_header.setStyleSheet("background-color: white")
        self.lbl_header.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header.setObjectName("lbl_header")
        self.lbl_text = QtWidgets.QLabel(self.instruction)
        self.lbl_text.setGeometry(QtCore.QRect(80, 160, 831, 661))
        self.lbl_text.setObjectName("lbl_text")
        self.stackedWidget.addWidget(self.instruction)
        self.unit_converter_page = QtWidgets.QWidget()
        self.unit_converter_page.setObjectName("unit_converter_page")
        self.lbl_header_unit = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_header_unit.setGeometry(QtCore.QRect(150, 50, 251, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_header_unit.setFont(font)
        self.lbl_header_unit.setStyleSheet("background-color: white")
        self.lbl_header_unit.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header_unit.setObjectName("lbl_header_unit")
        self.lbl_equally = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_equally.setGeometry(QtCore.QRect(260, 150, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lbl_equally.setFont(font)
        self.lbl_equally.setStyleSheet("background-color: black; color: white;")
        self.lbl_equally.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_equally.setObjectName("lbl_equally")
        self.btn_count = QtWidgets.QPushButton(self.unit_converter_page)
        self.btn_count.setGeometry(QtCore.QRect(40, 300, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.btn_count.setFont(font)
        self.btn_count.setStyleSheet("background-color: white")
        self.btn_count.setObjectName("btn_count")
        self.cb_units_of_length = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_length.setGeometry(QtCore.QRect(10, 230, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_length.setFont(font)
        self.cb_units_of_length.setStyleSheet("background-color: white")
        self.cb_units_of_length.setObjectName("cb_units_of_length")
        self.cb_units_of_length.addItem("")
        self.cb_units_of_length.addItem("")
        self.cb_units_of_length.addItem("")
        self.cb_units_of_length.addItem("")
        self.cb_units_of_length_2 = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_length_2.setGeometry(QtCore.QRect(310, 230, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_length_2.setFont(font)
        self.cb_units_of_length_2.setStyleSheet("background-color:white")
        self.cb_units_of_length_2.setObjectName("cb_units_of_length_2")
        self.cb_units_of_length_2.addItem("")
        self.cb_units_of_length_2.addItem("")
        self.cb_units_of_length_2.addItem("")
        self.cb_units_of_length_2.addItem("")
        self.le_units_of_length = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_length.setGeometry(QtCore.QRect(10, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_length.setFont(font)
        self.le_units_of_length.setStyleSheet("background-color: white")
        self.le_units_of_length.setObjectName("le_units_of_length")
        self.le_units_of_length_2 = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_length_2.setGeometry(QtCore.QRect(310, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_length_2.setFont(font)
        self.le_units_of_length_2.setStyleSheet("background-color: white")
        self.le_units_of_length_2.setObjectName("le_units_of_length_2")
        self.lbl_rezult = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_rezult.setGeometry(QtCore.QRect(320, 300, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_rezult.setFont(font)
        self.lbl_rezult.setStyleSheet("background-color: white")
        self.lbl_rezult.setText("")
        self.lbl_rezult.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rezult.setObjectName("lbl_rezult")
        self.line = QtWidgets.QFrame(self.unit_converter_page)
        self.line.setGeometry(QtCore.QRect(0, 460, 1191, 5))
        self.line.setStyleSheet("background-color: white")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.unit_converter_page)
        self.line_2.setGeometry(QtCore.QRect(610, 10, 5, 881))
        self.line_2.setStyleSheet("background-color: white")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lbl_header_mass = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_header_mass.setGeometry(QtCore.QRect(140, 510, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_header_mass.setFont(font)
        self.lbl_header_mass.setStyleSheet("background-color: white")
        self.lbl_header_mass.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header_mass.setObjectName("lbl_header_mass")
        self.lbl_header_square = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_header_square.setGeometry(QtCore.QRect(790, 50, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_header_square.setFont(font)
        self.lbl_header_square.setStyleSheet("background-color: white")
        self.lbl_header_square.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header_square.setObjectName("lbl_header_square")
        self.lbl_header_time = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_header_time.setGeometry(QtCore.QRect(800, 510, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_header_time.setFont(font)
        self.lbl_header_time.setStyleSheet("background-color: white")
        self.lbl_header_time.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header_time.setObjectName("lbl_header_time")
        self.le_units_of_mass = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_mass.setGeometry(QtCore.QRect(20, 600, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_mass.setFont(font)
        self.le_units_of_mass.setStyleSheet("background-color: white")
        self.le_units_of_mass.setObjectName("le_units_of_mass")
        self.le_units_of_mass_2 = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_mass_2.setGeometry(QtCore.QRect(310, 600, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_mass_2.setFont(font)
        self.le_units_of_mass_2.setStyleSheet("background-color: white")
        self.le_units_of_mass_2.setObjectName("le_units_of_mass_2")
        self.lbl_equally_2 = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_equally_2.setGeometry(QtCore.QRect(250, 610, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lbl_equally_2.setFont(font)
        self.lbl_equally_2.setStyleSheet("background-color: black; color: white;")
        self.lbl_equally_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_equally_2.setObjectName("lbl_equally_2")
        self.cb_units_of_mass = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_mass.setGeometry(QtCore.QRect(20, 690, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_mass.setFont(font)
        self.cb_units_of_mass.setStyleSheet("background-color: white")
        self.cb_units_of_mass.setObjectName("cb_units_of_mass")
        self.cb_units_of_mass.addItem("")
        self.cb_units_of_mass.addItem("")
        self.cb_units_of_mass.addItem("")
        self.cb_units_of_mass.addItem("")
        self.cb_units_of_mass_2 = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_mass_2.setGeometry(QtCore.QRect(310, 690, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_mass_2.setFont(font)
        self.cb_units_of_mass_2.setStyleSheet("background-color: white")
        self.cb_units_of_mass_2.setObjectName("cb_units_of_mass_2")
        self.cb_units_of_mass_2.addItem("")
        self.cb_units_of_mass_2.addItem("")
        self.cb_units_of_mass_2.addItem("")
        self.btn_count_2 = QtWidgets.QPushButton(self.unit_converter_page)
        self.btn_count_2.setGeometry(QtCore.QRect(40, 770, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.btn_count_2.setFont(font)
        self.btn_count_2.setStyleSheet("background-color: white")
        self.btn_count_2.setObjectName("btn_count_2")
        self.lbl_rezult_2 = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_rezult_2.setGeometry(QtCore.QRect(310, 770, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_rezult_2.setFont(font)
        self.lbl_rezult_2.setStyleSheet("background-color: white")
        self.lbl_rezult_2.setText("")
        self.lbl_rezult_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rezult_2.setObjectName("lbl_rezult_2")
        self.btn_count_3 = QtWidgets.QPushButton(self.unit_converter_page)
        self.btn_count_3.setGeometry(QtCore.QRect(690, 300, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.btn_count_3.setFont(font)
        self.btn_count_3.setStyleSheet("background-color: white")
        self.btn_count_3.setObjectName("btn_count_3")
        self.lbl_rezult_3 = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_rezult_3.setGeometry(QtCore.QRect(940, 300, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_rezult_3.setFont(font)
        self.lbl_rezult_3.setStyleSheet("background-color: white")
        self.lbl_rezult_3.setText("")
        self.lbl_rezult_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rezult_3.setObjectName("lbl_rezult_3")
        self.lbl_equally_3 = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_equally_3.setGeometry(QtCore.QRect(900, 150, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lbl_equally_3.setFont(font)
        self.lbl_equally_3.setStyleSheet("background-color: black; color: white;")
        self.lbl_equally_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_equally_3.setObjectName("lbl_equally_3")
        self.le_units_of_square = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_square.setGeometry(QtCore.QRect(650, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_square.setFont(font)
        self.le_units_of_square.setStyleSheet("background-color: white")
        self.le_units_of_square.setObjectName("le_units_of_square")
        self.le_units_of_square_2 = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_square_2.setGeometry(QtCore.QRect(950, 150, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_square_2.setFont(font)
        self.le_units_of_square_2.setStyleSheet("background-color: white")
        self.le_units_of_square_2.setObjectName("le_units_of_square_2")
        self.cb_units_of_square = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_square.setGeometry(QtCore.QRect(650, 230, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_square.setFont(font)
        self.cb_units_of_square.setStyleSheet("background-color: white")
        self.cb_units_of_square.setObjectName("cb_units_of_square")
        self.cb_units_of_square.addItem("")
        self.cb_units_of_square.addItem("")
        self.cb_units_of_square.addItem("")
        self.cb_units_of_square.addItem("")
        self.cb_units_of_square.addItem("")
        self.cb_units_of_square.addItem("")
        self.cb_units_of_square_2 = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_square_2.setGeometry(QtCore.QRect(950, 230, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_square_2.setFont(font)
        self.cb_units_of_square_2.setStyleSheet("background-color: white")
        self.cb_units_of_square_2.setObjectName("cb_units_of_square_2")
        self.cb_units_of_square_2.addItem("")
        self.cb_units_of_square_2.addItem("")
        self.cb_units_of_square_2.addItem("")
        self.cb_units_of_square_2.addItem("")
        self.cb_units_of_square_2.addItem("")
        self.cb_units_of_square_2.addItem("")
        self.le_units_of_time = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_time.setGeometry(QtCore.QRect(630, 600, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_time.setFont(font)
        self.le_units_of_time.setStyleSheet("background-color: white")
        self.le_units_of_time.setObjectName("le_units_of_time")
        self.le_units_of_time_2 = QtWidgets.QLineEdit(self.unit_converter_page)
        self.le_units_of_time_2.setGeometry(QtCore.QRect(950, 600, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_units_of_time_2.setFont(font)
        self.le_units_of_time_2.setStyleSheet("background-color: white")
        self.le_units_of_time_2.setObjectName("le_units_of_time_2")
        self.lbl_equally_4 = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_equally_4.setGeometry(QtCore.QRect(890, 610, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.lbl_equally_4.setFont(font)
        self.lbl_equally_4.setStyleSheet("background-color: black; color: white;")
        self.lbl_equally_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_equally_4.setObjectName("lbl_equally_4")
        self.cb_units_of_time = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_time.setGeometry(QtCore.QRect(630, 690, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_time.setFont(font)
        self.cb_units_of_time.setStyleSheet("background-color: white")
        self.cb_units_of_time.setObjectName("cb_units_of_time")
        self.cb_units_of_time.addItem("")
        self.cb_units_of_time.addItem("")
        self.cb_units_of_time.addItem("")
        self.cb_units_of_time.addItem("")
        self.cb_units_of_time.addItem("")
        self.cb_units_of_time_2 = QtWidgets.QComboBox(self.unit_converter_page)
        self.cb_units_of_time_2.setGeometry(QtCore.QRect(950, 690, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_time_2.setFont(font)
        self.cb_units_of_time_2.setStyleSheet("background-color: white")
        self.cb_units_of_time_2.setObjectName("cb_units_of_time_2")
        self.cb_units_of_time_2.addItem("")
        self.cb_units_of_time_2.addItem("")
        self.cb_units_of_time_2.addItem("")
        self.cb_units_of_time_2.addItem("")
        self.cb_units_of_time_2.addItem("")
        self.btn_count_4 = QtWidgets.QPushButton(self.unit_converter_page)
        self.btn_count_4.setGeometry(QtCore.QRect(660, 770, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        self.btn_count_4.setFont(font)
        self.btn_count_4.setStyleSheet("background-color: white")
        self.btn_count_4.setObjectName("btn_count_4")
        self.lbl_rezult_4 = QtWidgets.QLabel(self.unit_converter_page)
        self.lbl_rezult_4.setGeometry(QtCore.QRect(950, 760, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_rezult_4.setFont(font)
        self.lbl_rezult_4.setStyleSheet("background-color: white")
        self.lbl_rezult_4.setText("")
        self.lbl_rezult_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rezult_4.setObjectName("lbl_rezult_4")
        self.stackedWidget.addWidget(self.unit_converter_page)
        self.ratio_converter_page = QtWidgets.QWidget()
        self.ratio_converter_page.setObjectName("ratio_converter_page")
        self.lbl_header_ratio = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_header_ratio.setGeometry(QtCore.QRect(210, 20, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_header_ratio.setFont(font)
        self.lbl_header_ratio.setStyleSheet("background-color: white")
        self.lbl_header_ratio.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header_ratio.setObjectName("lbl_header_ratio")
        self.lbl_pa = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_pa.setGeometry(QtCore.QRect(50, 450, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_pa.setFont(font)
        self.lbl_pa.setStyleSheet("background-color: white")
        self.lbl_pa.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pa.setObjectName("lbl_pa")
        self.lbl_kpa = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_kpa.setGeometry(QtCore.QRect(310, 450, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_kpa.setFont(font)
        self.lbl_kpa.setStyleSheet("background-color: white")
        self.lbl_kpa.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_kpa.setObjectName("lbl_kpa")
        self.lbl_mpa = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_mpa.setGeometry(QtCore.QRect(540, 450, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_mpa.setFont(font)
        self.lbl_mpa.setStyleSheet("background-color: white")
        self.lbl_mpa.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mpa.setObjectName("lbl_mpa")
        self.lbl_kgs = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_kgs.setGeometry(QtCore.QRect(760, 450, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_kgs.setFont(font)
        self.lbl_kgs.setStyleSheet("background-color: white")
        self.lbl_kgs.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_kgs.setObjectName("lbl_kgs")
        self.lbl_fiz = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_fiz.setGeometry(QtCore.QRect(990, 450, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_fiz.setFont(font)
        self.lbl_fiz.setStyleSheet("background-color: white")
        self.lbl_fiz.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_fiz.setObjectName("lbl_fiz")
        self.lbl_mmrtst = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_mmrtst.setGeometry(QtCore.QRect(50, 710, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_mmrtst.setFont(font)
        self.lbl_mmrtst.setStyleSheet("background-color: white")
        self.lbl_mmrtst.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mmrtst.setObjectName("lbl_mmrtst")
        self.lbl_mmvodst = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_mmvodst.setGeometry(QtCore.QRect(250, 710, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_mmvodst.setFont(font)
        self.lbl_mmvodst.setStyleSheet("background-color: white")
        self.lbl_mmvodst.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_mmvodst.setObjectName("lbl_mmvodst")
        self.lbl_bar = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_bar.setGeometry(QtCore.QRect(470, 710, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_bar.setFont(font)
        self.lbl_bar.setStyleSheet("background-color: white")
        self.lbl_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_bar.setObjectName("lbl_bar")
        self.lbl_psi = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_psi.setGeometry(QtCore.QRect(660, 710, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_psi.setFont(font)
        self.lbl_psi.setStyleSheet("background-color: white")
        self.lbl_psi.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_psi.setObjectName("lbl_psi")
        self.cb_units_of_pressures = QtWidgets.QComboBox(self.ratio_converter_page)
        self.cb_units_of_pressures.setGeometry(QtCore.QRect(430, 160, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.cb_units_of_pressures.setFont(font)
        self.cb_units_of_pressures.setStyleSheet("background-color: white")
        self.cb_units_of_pressures.setObjectName("cb_units_of_pressures")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.cb_units_of_pressures.addItem("")
        self.btn_count_5 = QtWidgets.QPushButton(self.ratio_converter_page)
        self.btn_count_5.setGeometry(QtCore.QRect(440, 310, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.btn_count_5.setFont(font)
        self.btn_count_5.setStyleSheet("background-color: white")
        self.btn_count_5.setObjectName("btn_count_5")
        self.lbl_rez_1 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_1.setGeometry(QtCore.QRect(30, 540, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_1.setFont(font)
        self.lbl_rez_1.setStyleSheet("background-color: white")
        self.lbl_rez_1.setText("")
        self.lbl_rez_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_1.setObjectName("lbl_rez_1")
        self.lbl_rez_2 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_2.setGeometry(QtCore.QRect(280, 540, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_2.setFont(font)
        self.lbl_rez_2.setStyleSheet("background-color: white")
        self.lbl_rez_2.setText("")
        self.lbl_rez_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_2.setObjectName("lbl_rez_2")
        self.lbl_rez_3 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_3.setGeometry(QtCore.QRect(510, 540, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_3.setFont(font)
        self.lbl_rez_3.setStyleSheet("background-color: white")
        self.lbl_rez_3.setText("")
        self.lbl_rez_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_3.setObjectName("lbl_rez_3")
        self.lbl_rez_4 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_4.setGeometry(QtCore.QRect(740, 540, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_4.setFont(font)
        self.lbl_rez_4.setStyleSheet("background-color: white")
        self.lbl_rez_4.setText("")
        self.lbl_rez_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_4.setObjectName("lbl_rez_4")
        self.lbl_rez_5 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_5.setGeometry(QtCore.QRect(970, 540, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_5.setFont(font)
        self.lbl_rez_5.setStyleSheet("background-color: white")
        self.lbl_rez_5.setText("")
        self.lbl_rez_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_5.setObjectName("lbl_rez_5")
        self.lbl_rez_6 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_6.setGeometry(QtCore.QRect(30, 800, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_6.setFont(font)
        self.lbl_rez_6.setStyleSheet("background-color: white")
        self.lbl_rez_6.setText("")
        self.lbl_rez_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_6.setObjectName("lbl_rez_6")
        self.lbl_rez_7 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_7.setGeometry(QtCore.QRect(240, 800, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_7.setFont(font)
        self.lbl_rez_7.setStyleSheet("background-color: white")
        self.lbl_rez_7.setText("")
        self.lbl_rez_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_7.setObjectName("lbl_rez_7")
        self.lbl_rez_8 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_8.setGeometry(QtCore.QRect(450, 800, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_8.setFont(font)
        self.lbl_rez_8.setStyleSheet("background-color: white")
        self.lbl_rez_8.setText("")
        self.lbl_rez_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_8.setObjectName("lbl_rez_8")
        self.lbl_rez_9 = QtWidgets.QLabel(self.ratio_converter_page)
        self.lbl_rez_9.setGeometry(QtCore.QRect(650, 800, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.lbl_rez_9.setFont(font)
        self.lbl_rez_9.setStyleSheet("background-color: white")
        self.lbl_rez_9.setText("")
        self.lbl_rez_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_rez_9.setObjectName("lbl_rez_9")
        self.le_get_data = QtWidgets.QLineEdit(self.ratio_converter_page)
        self.le_get_data.setGeometry(QtCore.QRect(430, 240, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.le_get_data.setFont(font)
        self.le_get_data.setStyleSheet("background-color: white")
        self.le_get_data.setObjectName("le_get_data")
        self.stackedWidget.addWidget(self.ratio_converter_page)
        self.calculator_page = QtWidgets.QWidget()
        self.calculator_page.setObjectName("calculator_page")
        self.lbl_header_calculator = QtWidgets.QLabel(self.calculator_page)
        self.lbl_header_calculator.setGeometry(QtCore.QRect(360, 40, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.lbl_header_calculator.setFont(font)
        self.lbl_header_calculator.setStyleSheet("background-color:white")
        self.lbl_header_calculator.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_header_calculator.setObjectName("lbl_header_calculator")
        self.stackedWidget.addWidget(self.calculator_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_unit_converter.setText(_translate("MainWindow", "Конвертер единиц"))
        self.btn_calculator.setText(_translate("MainWindow", "Калькулятор"))
        self.btn_ratio_converter.setText(_translate("MainWindow", "Конвертер давления"))
        self.lbl_header.setText(_translate("MainWindow", "Инструкция"))
        self.lbl_text.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_header_unit.setText(_translate("MainWindow", "Единицы длины"))
        self.lbl_equally.setText(_translate("MainWindow", "="))
        self.btn_count.setText(_translate("MainWindow", "Счёт"))
        self.cb_units_of_length.setItemText(0, _translate("MainWindow", "Сантиметр"))
        self.cb_units_of_length.setItemText(1, _translate("MainWindow", "Дециметр"))
        self.cb_units_of_length.setItemText(2, _translate("MainWindow", "Метр"))
        self.cb_units_of_length.setItemText(3, _translate("MainWindow", "Километр"))
        self.cb_units_of_length_2.setItemText(0, _translate("MainWindow", "Миллиметр"))
        self.cb_units_of_length_2.setItemText(1, _translate("MainWindow", "Сантиметр"))
        self.cb_units_of_length_2.setItemText(2, _translate("MainWindow", "Дециметр"))
        self.cb_units_of_length_2.setItemText(3, _translate("MainWindow", "Метр"))
        self.lbl_header_mass.setText(_translate("MainWindow", "Единицы массы"))
        self.lbl_header_square.setText(_translate("MainWindow", "Единицы площади"))
        self.lbl_header_time.setText(_translate("MainWindow", "Единицы времени"))
        self.lbl_equally_2.setText(_translate("MainWindow", "="))
        self.cb_units_of_mass.setItemText(0, _translate("MainWindow", "Килограмм"))
        self.cb_units_of_mass.setItemText(1, _translate("MainWindow", "Грамм"))
        self.cb_units_of_mass.setItemText(2, _translate("MainWindow", "Центнер"))
        self.cb_units_of_mass.setItemText(3, _translate("MainWindow", "Тонна"))
        self.cb_units_of_mass_2.setItemText(0, _translate("MainWindow", "Килограмм"))
        self.cb_units_of_mass_2.setItemText(1, _translate("MainWindow", "Грамм"))
        self.cb_units_of_mass_2.setItemText(2, _translate("MainWindow", "Центнер"))
        self.btn_count_2.setText(_translate("MainWindow", "Счёт"))
        self.btn_count_3.setText(_translate("MainWindow", "Счёт"))
        self.lbl_equally_3.setText(_translate("MainWindow", "="))
        self.cb_units_of_square.setItemText(0, _translate("MainWindow", "Сантиметр2"))
        self.cb_units_of_square.setItemText(1, _translate("MainWindow", "Дециметр2"))
        self.cb_units_of_square.setItemText(2, _translate("MainWindow", "Метр2"))
        self.cb_units_of_square.setItemText(3, _translate("MainWindow", "Километр2"))
        self.cb_units_of_square.setItemText(4, _translate("MainWindow", "Ар"))
        self.cb_units_of_square.setItemText(5, _translate("MainWindow", "Гектар"))
        self.cb_units_of_square_2.setItemText(0, _translate("MainWindow", "Миллиметр2"))
        self.cb_units_of_square_2.setItemText(1, _translate("MainWindow", "Сантиметр2"))
        self.cb_units_of_square_2.setItemText(2, _translate("MainWindow", "Дециметр2"))
        self.cb_units_of_square_2.setItemText(3, _translate("MainWindow", "Метр2"))
        self.cb_units_of_square_2.setItemText(4, _translate("MainWindow", "Ар"))
        self.cb_units_of_square_2.setItemText(5, _translate("MainWindow", "Гектар"))
        self.lbl_equally_4.setText(_translate("MainWindow", "="))
        self.cb_units_of_time.setItemText(0, _translate("MainWindow", "Минута"))
        self.cb_units_of_time.setItemText(1, _translate("MainWindow", "Час"))
        self.cb_units_of_time.setItemText(2, _translate("MainWindow", "Сутки"))
        self.cb_units_of_time.setItemText(3, _translate("MainWindow", "Год"))
        self.cb_units_of_time.setItemText(4, _translate("MainWindow", "Век"))
        self.cb_units_of_time_2.setItemText(0, _translate("MainWindow", "Секунда"))
        self.cb_units_of_time_2.setItemText(1, _translate("MainWindow", "Минута"))
        self.cb_units_of_time_2.setItemText(2, _translate("MainWindow", "Час"))
        self.cb_units_of_time_2.setItemText(3, _translate("MainWindow", "Месяц"))
        self.cb_units_of_time_2.setItemText(4, _translate("MainWindow", "Лет"))
        self.btn_count_4.setText(_translate("MainWindow", "Счёт"))
        self.lbl_header_ratio.setText(_translate("MainWindow", "Конвертер соотношения единиц измерения давления."))
        self.lbl_pa.setText(_translate("MainWindow", "Па"))
        self.lbl_kpa.setText(_translate("MainWindow", "кПа"))
        self.lbl_mpa.setText(_translate("MainWindow", "МПа"))
        self.lbl_kgs.setText(_translate("MainWindow", "кГс/см2"))
        self.lbl_fiz.setText(_translate("MainWindow", "физ.атм"))
        self.lbl_mmrtst.setText(_translate("MainWindow", "мм.рт.ст"))
        self.lbl_mmvodst.setText(_translate("MainWindow", "мм.вод.ст"))
        self.lbl_bar.setText(_translate("MainWindow", "bar"))
        self.lbl_psi.setText(_translate("MainWindow", "psi"))
        self.cb_units_of_pressures.setItemText(0, _translate("MainWindow", "Па"))
        self.cb_units_of_pressures.setItemText(1, _translate("MainWindow", "кПа"))
        self.cb_units_of_pressures.setItemText(2, _translate("MainWindow", "МПа"))
        self.cb_units_of_pressures.setItemText(3, _translate("MainWindow", "кГс/см2"))
        self.cb_units_of_pressures.setItemText(4, _translate("MainWindow", "физ.атм"))
        self.cb_units_of_pressures.setItemText(5, _translate("MainWindow", "мм.рт.ст"))
        self.cb_units_of_pressures.setItemText(6, _translate("MainWindow", "мм.вод.ст"))
        self.cb_units_of_pressures.setItemText(7, _translate("MainWindow", "bar"))
        self.cb_units_of_pressures.setItemText(8, _translate("MainWindow", "psi"))
        self.btn_count_5.setText(_translate("MainWindow", "Счёт"))
        self.lbl_header_calculator.setText(_translate("MainWindow", "Калькулятор"))
