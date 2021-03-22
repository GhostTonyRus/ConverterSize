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
        # счёт единиц длины
        self.ui.btn_count.clicked.connect(lambda: self.getLength(value_1=self.ui.cb_units_of_length.currentText(),
                                                                 value_2=self.ui.cb_units_of_length_2.currentText(),
                                                                 number_1=self.ui.le_units_of_length.text(),
                                                                 number_2=self.ui.le_units_of_length_2.text()))

        # счёт единиц массы
        self.ui.btn_count_2.clicked.connect(lambda: self.getMass(value_1=self.ui.cb_units_of_mass.currentText(),
                                                                 value_2=self.ui.cb_units_of_mass_2.currentText(),
                                                                 number_1=self.ui.le_units_of_mass.text(),
                                                                 number_2=self.ui.le_units_of_mass_2.text()))

        # счёт единиц площади
        self.ui.btn_count_3.clicked.connect(lambda: self.getSquare(value_1=self.ui.cb_units_of_square.currentText(),
                                                                   value_2=self.ui.cb_units_of_square_2.currentText(),
                                                                   number_1=self.ui.le_units_of_square.text(),
                                                                   number_2=self.ui.le_units_of_square_2.text()))

        # счёт единиц времени
        self.ui.btn_count_4.clicked.connect(lambda: self.getTime(value_1=self.ui.cb_units_of_time.currentText(),
                                                                 value_2=self.ui.cb_units_of_time_2.currentText(),
                                                                 number_1=self.ui.le_units_of_time.text(),
                                                                 number_2=self.ui.le_units_of_time_2.text()))

    # настройка показа окон
    # конвертер единиц
    def showUnitPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.unit_converter_page)

    # конвертер единиц давления
    def showRatioPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ratio_converter_page)

    # калькулятор
    def showCalculatorPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.calculator_page)


app = QtWidgets.QApplication(sys.argv)
application = MyWindow()
application.show()
sys.exit(app.exec_())
