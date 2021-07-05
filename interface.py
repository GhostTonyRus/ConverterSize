import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QDesktopWidget
from PyQt5.QtCore import  QPoint
from PyQt5.QtGui import QPixmap

from logic import Calculator
from main_ui import Ui_MainWindow
from progressbar_ui import Ui_LoardingScreen
from exit_window_ui import Ui_Exit_window_ui
import time

# myappid = 'myconverter.version.2.1.0'
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# начальный экран
class LoardingScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoardingScreen, self).__init__()

        self.ui = Ui_LoardingScreen()
        self.ui.setupUi(self)

        # автоматический запуск программы
        # QtCore.QTimer.singleShot(500, lambda: self.doAction())

        # настройка рамки окна
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_AttributeCount)
        self.setWindowIcon(QtGui.QIcon("C:\PycharmProjects\ConverterSize\\resources\icon.png"))
        self.setWindowTitle("Инженерный переводчик")

        # показывает страницу авторизации
        self.ui.stackedWidget.setCurrentWidget(self.ui.login_page)

        # настройка поля ввода
        self.ui.le_password_input.setEchoMode(QtWidgets.QLineEdit.Password)

        # настройка кнопки ввода
        self.ui.btn_login.clicked.connect(lambda: self.checkPassord())
        self.ui.btn_login.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_password_input.returnPressed.connect(self.ui.btn_login.click)  # нажатие <Enter>

        # настройка иконки
        icon = QPixmap("C:\PycharmProjects\ConverterSize\\resources\miniicon.png")
        icon.size()
        self.ui.lbl_icon.setPixmap(icon)

        # кнопка сворачивания программв
        self.ui.btn_roll_up.clicked.connect(lambda: self.showMinimized())

        # настройки кнопки выхода
        self.ui.btn_close.clicked.connect(self.close)

    # роверка введённого пароля
    def checkPasswordInput(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Введите верный пароль!")
        self.ui.le_password_input.clear()
        exit = msg.exec_()

    # запуск главного окна программы
    def doAction(self):
        for i in range(101):
            time.sleep(0.01)
            self.ui.progressBar.setProperty("value", i)
            if i == 100:
                time.sleep(1)
                self.main_window = MyWindow()
                self.main_window.show()
                self.close()

    # проверка пароля
    def checkPassord(self):
        text = self.ui.le_password_input.text()
        if text == "чёрт":
            self.ui.stackedWidget.setCurrentWidget(self.ui.loarding_page)
            self.doAction()
        else:
            self.checkPasswordInput()

    # перетаскивание окна
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

# экран с подтверждение выхода из программы
class ExitWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Exit_window_ui()
        self.ui.setupUi(self)

        # скрываем элементы
        self.ui.progressBar.close()

        # настройка рамки окна
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_AttributeCount)
        self.setWindowIcon(QtGui.QIcon("C:\PycharmProjects\ConverterSize\\resources\icon.png"))
        self.setWindowTitle("Инженерный переводчик")

        # настройка иконки
        icon = QPixmap("C:\PycharmProjects\ConverterSize\\resources\miniicon.png")
        icon.size()
        self.ui.lbl_icon.setPixmap(icon)

        # настройка кнопок
        self.ui.btn_yes.clicked.connect(lambda: self.close_app())
        self.ui.btn_no.clicked.connect(lambda: self.close())

        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_roll_up.clicked.connect(lambda: self.showMinimized())


    def close_app(self):
        self.ui.lbl_description.setText("Выход...")
        self.ui.progressBar.show()
        for i in range(101):
            time.sleep(0.01)
            self.ui.progressBar.setProperty("value", i)
            if i == 100:
                sys.exit()

    # перетаскивание окна
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


# основное окно программы
class MyWindow(QtWidgets.QMainWindow, Calculator):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # настройка рамки окна
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_AttributeCount)
        self.setWindowIcon(QtGui.QIcon("C:\PycharmProjects\ConverterSize\\resources\icon.png"))
        self.setWindowTitle("Инженерный переводчик")

        # показ окна инструкции по умолчанию
        self.ui.stackedWidget.setCurrentWidget(self.ui.instruction)

        # настройка кнопок
        # показ конвертора единиц
        # self.ui.btn_unit_converter.clicked.connect(self.showUnitPage) - временно не используется
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
        self.ui.btn_count_5.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_get_data.returnPressed.connect(self.ui.btn_count_5.click)  # нажатие <Enter>

        # перевод единиц длины
        self.ui.btn_conversion_1.clicked.connect(
            lambda: self.conversionLength(number=self.ui.le_units_of_length_3.text(),
                                          value_1=self.ui.cb_units_of_length_3.currentText(),
                                          value_2=self.ui.cb_units_of_length_4.currentText()))
        self.ui.btn_conversion_1.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_units_of_length_3.returnPressed.connect(self.ui.btn_conversion_1.click)  # нажатие <Enter>


        # перевод единиц площади
        self.ui.btn_conversion_2.clicked.connect(
            lambda: self.conversionSquare(number=self.ui.le_units_of_square_3.text(),
                                          value_1=self.ui.cb_units_of_square_3.currentText(),
                                          value_2=self.ui.cb_units_of_square_4.currentText()))
        self.ui.btn_conversion_2.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_units_of_square_3.returnPressed.connect(self.ui.btn_conversion_2.click)  # нажатие <Enter>


        # перевод единиц массы
        self.ui.btn_conversion_3.clicked.connect(lambda: self.conversionMass(number=self.ui.le_units_of_mass_3.text(),
                                                                             value_1=self.ui.cb_units_of_mass_3.currentText(),
                                                                             value_2=self.ui.cb_units_of_mass_4.currentText()))
        self.ui.btn_conversion_3.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_units_of_mass_3.returnPressed.connect(self.ui.btn_conversion_3.click)  # нажатие <Enter>


        # перевод единиц времени
        self.ui.btn_conversion_4.clicked.connect(lambda: self.conversionTime(number=self.ui.le_units_of_time_3.text(),
                                                                             value_1=self.ui.cb_units_of_time_3.currentText(),
                                                                             value_2=self.ui.cb_units_of_time_4.currentText()))
        self.ui.btn_conversion_4.setAutoDefault(True)  # нажатие <Enter>
        self.ui.le_units_of_time_3.returnPressed.connect(self.ui.btn_conversion_4.click)  # нажатие <Enter>

        # кнока закрытия программы
        self.ui.btn_close.clicked.connect(lambda: self.exit())

        # кнопка сворачивания программв
        self.ui.btn_roll_up.clicked.connect(lambda: self.showMinimized())

        # настройка иконки
        icon = QPixmap("C:\PycharmProjects\ConverterSize\\resources\miniicon.png")
        icon.size()
        self.ui.lbl_icon.setPixmap(icon)

        # настройка кнопок калькулятора
        self.ui.btn_0.clicked.connect(lambda: self.getValues(value=0))
        self.ui.btn_1.clicked.connect(lambda: self.getValues(value=1))
        self.ui.btn_2.clicked.connect(lambda: self.getValues(value=2))
        self.ui.btn_3.clicked.connect(lambda: self.getValues(value=3))
        self.ui.btn_4.clicked.connect(lambda: self.getValues(value=4))
        self.ui.btn_5.clicked.connect(lambda: self.getValues(value=5))
        self.ui.btn_6.clicked.connect(lambda: self.getValues(value=6))
        self.ui.btn_7.clicked.connect(lambda: self.getValues(value=7))
        self.ui.btn_8.clicked.connect(lambda: self.getValues(value=8))
        self.ui.btn_9.clicked.connect(lambda: self.getValues(value=9))
        self.ui.btn_dot.clicked.connect(lambda: self.getValues(value="."))
        self.ui.btn_plus.clicked.connect(lambda: self.getValues(value="+"))
        self.ui.btn_minus.clicked.connect(lambda: self.getValues(value="-"))
        self.ui.btn_divide.clicked.connect(lambda: self.getValues(value="/"))
        self.ui.btn_multiply.clicked.connect(lambda: self.getValues(value="*"))
        self.ui.btn_exponentiation.clicked.connect(lambda: self.getValues(value="**"))
        self.ui.btn_left_bracket.clicked.connect(lambda: self.getValues(value="("))
        self.ui.btn_right_bracket.clicked.connect(lambda: self.getValues(value=")"))
        # self.ui.btn_sqrt.clicked.connect(lambda: self.getValues(value="√"))
        self.ui.btn_sqrt.clicked.connect(lambda: self.count_sqrt())
        self.ui.btn_equally.clicked.connect(lambda: self.insertRez())
        self.ui.btn_del.clicked.connect(lambda: self.ui.lbl_calc_rez.clear())  # очистка поля ввода
        # расчёт уголов
        self.ui.btn_sin.clicked.connect(lambda: self.count_sin()) # счёт sin
        self.ui.btn_cos.clicked.connect(lambda: self.count_cos()) # счёт sin
        self.ui.btn_tg.clicked.connect(lambda: self.count_tg()) # счёт tg
        self.ui.btn_ctg.clicked.connect(lambda: self.count_ctg()) # счёт ctg

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

    # окно с подтверждение выхода
    def exit(self):
        window = ExitWindow()
        window.show()




    # перетаскивание окна
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()