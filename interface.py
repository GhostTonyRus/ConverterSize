import sys

from PyQt5 import QtWidgets

from logic import Calculator
from main_ui import Ui_MainWindow


# pyuic5 main_ui.ui -o main_ui.py

class MyWindow(QtWidgets.QMainWindow, Calculator):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.calc = Calculator()

        self.ui.stackedWidget.setCurrentWidget(self.ui.instruction)

        # настройка кнопок
        # показ конвертора единиц
        self.ui.btn_unit_converter.clicked.connect(self.showUnitPage)
        self.ui.btn_ratio_converter.clicked.connect(self.showRatioPage)
        self.ui.btn_calculator.clicked.connect(self.showCalculatorPage)
        self.ui.btn_instruction.clicked.connect(self.showInstruction)
        # счёт единиц длины
        self.ui.btn_count.clicked.connect(lambda: self.getLength(value_1=self.ui.cb_units_of_length.currentText(), # единица из которой переводят
                                                                 value_2=self.ui.cb_units_of_length_2.currentText(), # единица в которую переводят
                                                                 number_1=self.ui.le_units_of_length.text(), # первое число для перевода
                                                                 number_2=self.ui.le_units_of_length_2.text())) # второе число для перевода

        # счёт единиц массы
        self.ui.btn_count_2.clicked.connect(lambda: self.getMass(value_1=self.ui.cb_units_of_mass.currentText(), # единица из которой переводят
                                                                 value_2=self.ui.cb_units_of_mass_2.currentText(),  # единица в которую переводят
                                                                 number_1=self.ui.le_units_of_mass.text(), # первое число для перевода
                                                                 number_2=self.ui.le_units_of_mass_2.text())) # второе число для перевода

        # счёт единиц площади
        self.ui.btn_count_3.clicked.connect(lambda: self.getSquare(value_1=self.ui.cb_units_of_square.currentText(), # единица из которой переводят
                                                                   value_2=self.ui.cb_units_of_square_2.currentText(), # единица в которую переводят
                                                                   number_1=self.ui.le_units_of_square.text(), # первое число для перевода
                                                                   number_2=self.ui.le_units_of_square_2.text())) # второе число для перевода

        # счёт единиц времени
        self.ui.btn_count_4.clicked.connect(lambda: self.getTime(value_1=self.ui.cb_units_of_time.currentText(), # единица из которой переводят
                                                                 value_2=self.ui.cb_units_of_time_2.currentText(), # единица в которую переводят
                                                                 number_1=self.ui.le_units_of_time.text(), # первое число для перевода
                                                                 number_2=self.ui.le_units_of_time_2.text())) # второе число для перевода

        # счёт единиц давления
        self.ui.btn_count_5.clicked.connect(lambda: self.getPressure(value=self.ui.cb_units_of_pressures.currentText()))

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

