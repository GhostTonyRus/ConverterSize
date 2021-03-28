import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTimer
from logic import Calculator
from main_ui import Ui_MainWindow
from progressbar_ui import Ui_LoardingScreen
import time


class LoardingScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoardingScreen, self).__init__()

        self.ui = Ui_LoardingScreen()
        self.ui.setupUi(self)

        # автоматический запуск программы
        QtCore.QTimer.singleShot(1500, lambda: self.doAction())

        # УДАЛЯЕМ РАМКИ
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_AttributeCount)

    def doAction(self):
        for i in range(101):
            time.sleep(0.05)
            self.ui.progressBar.setProperty("value", i)
            if i == 100:
                time.sleep(2)
                self.main_window = MyWindow()
                self.main_window.show()
                self.close()


class MyWindow(QtWidgets.QMainWindow, Calculator):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # прказ окна инструкции по умолчанию
        self.ui.stackedWidget.setCurrentWidget(self.ui.instruction)

        # настройка кнопок
        # показ конвертора единиц
        self.ui.btn_unit_converter.clicked.connect(self.showUnitPage)
        # показ давления
        self.ui.btn_ratio_converter.clicked.connect(self.showRatioPage)
        # показ калькулятор
        self.ui.btn_calculator.clicked.connect(self.showCalculatorPage)
        # показ инструкции
        self.ui.btn_instruction.clicked.connect(self.showInstruction)
        # показ конвертер 2
        self.ui.btn_converter_2.clicked.connect(self.showConverter)

        # счёт единиц длины
        self.ui.btn_count.clicked.connect(
            lambda: self.getLength(value_1=self.ui.cb_units_of_length.currentText(),  # единица из которой переводят
                                   value_2=self.ui.cb_units_of_length_2.currentText(),  # единица в которую переводят
                                   number_1=self.ui.le_units_of_length.text(),  # первое число для перевода
                                   number_2=self.ui.le_units_of_length_2.text()))  # второе число для перевода

        # счёт единиц массы
        self.ui.btn_count_2.clicked.connect(
            lambda: self.getMass(value_1=self.ui.cb_units_of_mass.currentText(),  # единица из которой переводят
                                 value_2=self.ui.cb_units_of_mass_2.currentText(),  # единица в которую переводят
                                 number_1=self.ui.le_units_of_mass.text(),  # первое число для перевода
                                 number_2=self.ui.le_units_of_mass_2.text()))  # второе число для перевода

        # счёт единиц площади
        self.ui.btn_count_3.clicked.connect(
            lambda: self.getSquare(value_1=self.ui.cb_units_of_square.currentText(),  # единица из которой переводят
                                   value_2=self.ui.cb_units_of_square_2.currentText(),  # единица в которую переводят
                                   number_1=self.ui.le_units_of_square.text(),  # первое число для перевода
                                   number_2=self.ui.le_units_of_square_2.text()))  # второе число для перевода

        # счёт единиц времени
        self.ui.btn_count_4.clicked.connect(
            lambda: self.getTime(value_1=self.ui.cb_units_of_time.currentText(),  # единица из которой переводят
                                 value_2=self.ui.cb_units_of_time_2.currentText(),  # единица в которую переводят
                                 number_1=self.ui.le_units_of_time.text(),  # первое число для перевода
                                 number_2=self.ui.le_units_of_time_2.text()))  # второе число для перевода

        # счёт единиц давления
        self.ui.btn_count_5.clicked.connect(lambda: self.getPressure(value=self.ui.cb_units_of_pressures.currentText()))

        # перевод единиц длины
        self.ui.btn_conversion_1.clicked.connect(
            lambda: self.conversionLength(number=self.ui.le_units_of_length_3.text(),
                                          value_1=self.ui.cb_units_of_length_3.currentText(),
                                          value_2=self.ui.cb_units_of_length_4.currentText()))
        # перевод единиц площпди
        self.ui.btn_conversion_2.clicked.connect(
            lambda: self.conversionSquare(number=self.ui.le_units_of_square_3.text(),
                                          value_1=self.ui.cb_units_of_square_3.currentText(),
                                          value_2=self.ui.cb_units_of_square_4.currentText()))
        # перевод единиц массы
        self.ui.btn_conversion_3.clicked.connect(lambda: self.conversionMass(number=self.ui.le_units_of_mass_3.text(),
                                                                             value_1=self.ui.cb_units_of_mass_3.currentText(),
                                                                             value_2=self.ui.cb_units_of_mass_4.currentText()))
        # перевод единиц времени
        self.ui.btn_conversion_4.clicked.connect(lambda: self.conversionTime(number=self.ui.le_units_of_time_3.text(),
                                                                             value_1=self.ui.cb_units_of_time_3.currentText(),
                                                                             value_2=self.ui.cb_units_of_time_4.currentText()))

    # настройка показа окон
    # страница конвертера единиц
    def showUnitPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.unit_converter_page)

    # страница конвертера единиц давления
    def showRatioPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ratio_converter_page)

    # страница калькулятора
    def showCalculatorPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.calculator_page)

    # страница инструкции
    def showInstruction(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.instruction)

    # страница конвертора 2
    def showConverter(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.unit_converter_page_2)
