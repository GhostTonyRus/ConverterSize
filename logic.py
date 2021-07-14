from PyQt5.QtWidgets import QMessageBox
from main_ui import Ui_MainWindow
import random
import math


class Calculator:
    ui = Ui_MainWindow()

    # проверка пустое поле или нет
    def showEmptyError(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("ПОЛЕ ВВОДА НЕ ДОЛЖНЫ БЫТЬ ПУСТЫМ!")
        # возбуждает исключение
        exit = msg.exec_()

    # возникает ошибка если введённое значение пцстое
    def showStrError(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("ВВЕДЁННОЕ ЗНАЧЕНИЕ ДОЛЖНО БЫТЬ ЧИСЛОМ!")
        exit = msg.exec_()

    # счёт длины
    def getLength(self, value_1, value_2, number_1, number_2):
        # проверка полей ввода
        if number_1 == "" or number_2 == "":
            self.showEmptyError()
        elif number_1.isalpha() or number_2.isalpha():
            self.showStrError()
        else:
            num_1 = float(number_1)
            num_2 = float(number_2)
            if value_1 == "Сантиметр" and value_2 == "Миллиметр":
                rez = num_1 * (num_2 * 10)
                self.ui.lbl_rezult.setText(str(rez))
            if value_1 == "Сантиметр" and value_2 == "Миллиметр":
                rez = num_1 * (num_2 * 10)
                self.ui.lbl_rezult.setText(str(rez))
            elif value_1 == "Дециметр" and value_2 == "Сантиметр":
                rez = num_1 * (num_2 * 10)
                self.ui.lbl_rezult.setText(str(rez))
            elif value_1 == "Дециметр" and value_2 == "Миллиметр":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult.setText(str(rez))
            elif value_1 == "Метр" and value_1 == "Сантиметр":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult.setText(str(rez))
            elif value_1 == "Метр" and value_1 == "Дециметр":
                rez = num_1 * (num_2 * 10)
                self.ui.lbl_rezult.setText(str(rez))
            elif value_1 == "Метр" and value_1 == "Миллиметр":
                rez = num_1 * (num_2 * 1000)
                self.ui.lbl_rezult.setText(str(rez))
            elif value_1 == "Километр" and value_2 == "Метр":
                rez = num_1 * (num_2 * 1000)
                self.ui.lbl_rezult.setText(str(rez))

    # счёт массы
    def getMass(self, value_1, value_2, number_1, number_2):
        # проверка полей ввода
        if number_1 == "" or number_2 == "":
            self.showEmptyError()
        else:
            num_1 = float(number_1)
            num_2 = float(number_2)
            if value_1 == "Килограмм" and value_2 == "Грамм":
                rez = num_1 * (num_2 * 1000)
                self.ui.lbl_rezult_2.setText(str(rez))
            elif value_1 == "Центнер" and value_2 == "Килограмм":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_2.setText(str(rez))
            elif value_1 == "Центнер" and value_2 == "Грамм":
                rez = num_1 * (num_2 * 100000)
                self.ui.lbl_rezult_2.setText(str(rez))
            elif value_1 == "Тонна" and value_2 == "Килограмм":
                rez = num_1 * (num_2 * 1000)
                self.ui.lbl_rezult_2.setText(str(rez))
            elif value_1 == "Тонна" and value_2 == "Центнер":
                rez = num_1 * (num_2 * 10)
                self.ui.lbl_rezult_2.setText(str(rez))

    # счёт площади
    def getSquare(self, value_1, value_2, number_1, number_2):
        # проверка полей ввода
        if number_1 == "" or number_2 == "":
            self.showEmptyError()
        else:
            num_1 = float(number_1)
            num_2 = float(number_2)
            if value_1 == "Сантиметр2" and value_2 == "Миллиметр2":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Дециметр2" and value_2 == "Сантиметр2":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Дециметр2" and value_2 == "Миллиметр2":
                rez = num_1 * (num_2 * 10000)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Метр2" and value_2 == "Сантиметр2":
                rez = num_1 * (num_2 * 10000)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Метр2" and value_2 == "Дециметр2":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Километр2" and value_2 == "Метр2":
                rez = num_1 * (num_2 * 1000000)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Ар" and value_2 == "Метр2":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Гектар" and value_2 == "Ар":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Километр2" and value_2 == "Гектар":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Километр2" and value_2 == "Ар":
                rez = num_1 * (num_2 * 10000)
                self.ui.lbl_rezult_3.setText(str(rez))
            elif value_1 == "Гектар" and value_2 == "Метр2":
                rez = num_1 * (num_2 * 10000)
                self.ui.lbl_rezult_3.setText(str(rez))

    # счёт времени
    def getTime(self, value_1, value_2, number_1, number_2):
        # проверка полей ввода
        if number_1 == "" or number_2 == "":
            self.showEmptyError()
        else:
            num_1 = float(number_1)
            num_2 = float(number_2)
            if value_1 == "Минута" and value_2 == "Секунда":
                rez = num_1 * (num_2 * 60)
                self.ui.lbl_rezult_4.setText(str(rez))
            elif value_1 == "Час" and value_2 == "Минута":
                rez = num_1 * (num_2 * 60)
                self.ui.lbl_rezult_4.setText(str(rez))
            elif value_1 == "Час" and value_2 == "Секунда":
                rez = num_1 * (num_2 * 3600)
                self.ui.lbl_rezult_4.setText(str(rez))
            elif value_1 == "Сутки" and value_2 == "Час":
                rez = num_1 * (num_2 * 24)
                self.ui.lbl_rezult_4.setText(str(rez))
            elif value_1 == "Год" and value_2 == "Месяц":
                rez = num_1 * (num_2 * 12)
                self.ui.lbl_rezult_4.setText(str(rez))
            elif value_1 == "Век" and value_2 == "Лет":
                rez = num_1 * (num_2 * 100)
                self.ui.lbl_rezult_4.setText(str(rez))

    # функция получает значение из поля формы и вызывает фунцию в соответствии с выбранным значением
    def getPressure(self, value):
        if value == "Па":
            self.count_pa(self.ui.le_get_data.text())
        elif value == "кПа":
            self.count_kPa(self.ui.le_get_data.text())
        elif value == "МПа":
            self.count_MPa(self.ui.le_get_data.text())
        elif value == "кГс/см2":
            self.count_kGs(self.ui.le_get_data.text())
        elif value == "физ.атм":
            self.count_fizatm(self.ui.le_get_data.text())
        elif value == "мм.рт.ст":
            self.count_mmrtst(self.ui.le_get_data.text())
        elif value == "мм.вод.ст":
            self.count_mmvodst(self.ui.le_get_data.text())
        elif value == "bar":
            self.count_bar(self.ui.le_get_data.text())
        elif value == "psi":
            self.count_psi(self.ui.le_get_data.text())

    # счёт Па
    def count_pa(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 1, self.ui.lbl_rez_kPa: 0.001, self.ui.lbl_rez_MPa: 0.000001,
            self.ui.lbl_rez_kGs_sm2: 0.0000102, self.ui.lbl_rez_fiz_atm: 0.00000987, self.ui.lbl_rez_mm_rt_st: 0.0075006,
            self.ui.lbl_rez_mm_vod_st: 0.101972, self.ui.lbl_rez_bar: 0.00001, self.ui.lbl_rez_psi: 0.00014504,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт кПа
    def count_kPa(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 1000, self.ui.lbl_rez_kPa: 1, self.ui.lbl_rez_MPa: 0.001,
            self.ui.lbl_rez_kGs_sm2: 0.0101972, self.ui.lbl_rez_fiz_atm: 0.00986923,
            self.ui.lbl_rez_mm_rt_st: 7.50062, self.ui.lbl_rez_mm_vod_st: 101.9716,
            self.ui.lbl_rez_bar: 0.01, self.ui.lbl_rez_psi: 0.1450377,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт МПа
    def count_MPa(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 10000000, self.ui.lbl_rez_kPa: 1000, self.ui.lbl_rez_MPa: 1,
            self.ui.lbl_rez_kGs_sm2: 10.19716, self.ui.lbl_rez_fiz_atm: 9.86923,
            self.ui.lbl_rez_mm_rt_st: 7500.62, self.ui.lbl_rez_mm_vod_st: 101971.6,
            self.ui.lbl_rez_bar: 10, self.ui.lbl_rez_psi: 145.0377,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт кГс/см2
    def count_kGs(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 98066.5, self.ui.lbl_rez_kPa: 98.0665, self.ui.lbl_rez_MPa: 0.0980665,
            self.ui.lbl_rez_kGs_sm2: 1, self.ui.lbl_rez_fiz_atm: 0.967841,
            self.ui.lbl_rez_mm_rt_st: 735.559, self.ui.lbl_rez_mm_vod_st: 100000,
            self.ui.lbl_rez_bar: 0.980665, self.ui.lbl_rez_psi: 14.223344,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт физ.атм
    def count_fizatm(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 101325, self.ui.lbl_rez_kPa: 101.325, self.ui.lbl_rez_MPa: 0.101325,
            self.ui.lbl_rez_kGs_sm2: 1.033227, self.ui.lbl_rez_fiz_atm: 1,
            self.ui.lbl_rez_mm_rt_st: 760, self.ui.lbl_rez_mm_vod_st: 10332.27,
            self.ui.lbl_rez_bar: 1.01325, self.ui.lbl_rez_psi: 14.6959,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт мм.рт.ст
    def count_mmrtst(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 133.3224, self.ui.lbl_rez_kPa: 0.1333224, self.ui.lbl_rez_MPa: 0.00011333,
            self.ui.lbl_rez_kGs_sm2: 0.0013595, self.ui.lbl_rez_fiz_atm: 0.00131579,
            self.ui.lbl_rez_mm_rt_st: 1, self.ui.lbl_rez_mm_vod_st: 13.6,
            self.ui.lbl_rez_bar: 0.00133322, self.ui.lbl_rez_psi: 0.019336,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт мм.вод.ст.
    def count_mmvodst(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 9.80665, self.ui.lbl_rez_kPa: 0.00980665, self.ui.lbl_rez_MPa: 0.00000981,
            self.ui.lbl_rez_kGs_sm2: 0.0001, self.ui.lbl_rez_fiz_atm: 0.00009678,
            self.ui.lbl_rez_mm_rt_st: 0.073556, self.ui.lbl_rez_mm_vod_st: 1,
            self.ui.lbl_rez_bar: 0.00009807, self.ui.lbl_rez_psi: 0.00142233,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт bar
    def count_bar(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 100000, self.ui.lbl_rez_kPa: 100, self.ui.lbl_rez_MPa: 0.1,
            self.ui.lbl_rez_kGs_sm2: 1.019716, self.ui.lbl_rez_fiz_atm: 0.986923,
            self.ui.lbl_rez_mm_rt_st: 750.062, self.ui.lbl_rez_mm_vod_st: 10197.16,
            self.ui.lbl_rez_bar: 1, self.ui.lbl_rez_psi: 14.50377,
        }
        for k, v in values.items():
            res = num * v
            k.setText(str(round(res, 2)))

    # счёт psi
    def count_psi(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        num = float(value)
        values = {
            self.ui.lbl_rez_Pa: 6894.757, self.ui.lbl_rez_kPa: 6.894757, self.ui.lbl_rez_MPa: 0.006894756,
            self.ui.lbl_rez_kGs_sm2: 0.070307, self.ui.lbl_rez_fiz_atm: 0.068046,
            self.ui.lbl_rez_mm_rt_st: 51.715217, self.ui.lbl_rez_mm_vod_st: 703.07,
            self.ui.lbl_rez_bar: 0.0689476, self.ui.lbl_rez_psi: 1,
        }
        for key, v in values.items():
            res = num * v
            key.setText(str(round(res, 2)))

    def conversation_length(self, *args, number):
        if number == "":
            self.showEmptyError()
        elif number.isalpha():
            self.showStrError()
        num = float(number)
        values = {"Сантиметр": 10, "Миллиметр": 1}
        # values = {"Сантиметр": 1}
        for k, v in values.items():
            for i in args:
                if k == i and k == i:
                    print(k)

    # перевод единиц длины
    def conversionLength(self, number, value_1, value_2):
        # проверка полей ввода
        if number == "":
            self.showEmptyError()
        elif number.isalpha():
            self.showStrError()
        else:
            num = float(number)
            if value_1 == "Сантиметр" and value_2 == "Миллиметр":
                rez1 = num * 10
                rez2 = num / 10
                self.ui.lbl_rezult_conversion.setText(str(rez1))
                self.ui.lbl_rezult_conversion_2.setText(str(rez2))
            elif value_1 == "Дециметр" and value_2 == "Сантиметр":
                rez1 = num * 10
                rez2 = num / 10
                self.ui.lbl_rezult_conversion.setText(str(rez1))
                self.ui.lbl_rezult_conversion_2.setText(str(rez2))
            elif value_1 == "Дециметр" and value_2 == "Миллиметр":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion.setText(str(rez1))
                self.ui.lbl_rezult_conversion_2.setText(str(rez2))
            elif value_1 == "Метр" and value_1 == "Сантиметр":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion.setText(str(rez1))
                self.ui.lbl_rezult_conversion_2.setText(str(rez2))
            elif value_1 == "Метр" and value_1 == "Дециметр":
                rez1 = num * 10
                rez2 = num / 10
                self.ui.lbl_rezult_conversion.setText(str(rez1))
                self.ui.lbl_rezult_conversion_2.setText(str(rez2))
            elif value_1 == "Метр" and value_1 == "Миллиметр":
                rez1 = num * 1000
                rez2 = num / 1000
                self.ui.lbl_rezult_conversion.setText(str(rez1))
                self.ui.lbl_rezult_conversion_2.setText(str(rez2))
            elif value_1 == "Километр" and value_2 == "Метр":
                rez1 = num * 1000
                rez2 = num / 1000
                self.ui.lbl_rezult_conversion.setText(str(rez1))
                self.ui.lbl_rezult_conversion_2.setText(str(rez2))

    # перевод единиц площади
    def conversionSquare(self, number, value_1, value_2):
        # проверка полей ввода
        if number == "":
            self.showEmptyError()
        elif number.isalpha():
            self.showStrError()
        else:
            num = float(number)
            if value_1 == "Сантиметр2" and value_2 == "Миллиметр2":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Дециметр2" and value_2 == "Сантиметр2":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Дециметр2" and value_2 == "Миллиметр2":
                rez1 = num * 10000
                rez2 = num / 10000
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Метр2" and value_2 == "Сантиметр2":
                rez1 = num * 10000
                rez2 = num / 10000
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Метр2" and value_2 == "Дециметр2":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Километр2" and value_2 == "Метр2":
                rez1 = num * 1000000
                rez2 = num / 1000000
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Ар" and value_2 == "Метр2":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Гектар" and value_2 == "Ар":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Километр2" and value_2 == "Гектар":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Километр2" and value_2 == "Ар":
                rez1 = num * 10000
                rez2 = num / 10000
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))
            elif value_1 == "Гектар" and value_2 == "Метр2":
                rez1 = num * 10000
                rez2 = num / 10000
                self.ui.lbl_rezult_conversion_3.setText(str(rez1))
                self.ui.lbl_rezult_conversion_4.setText(str(rez2))

    # перевод единиц массы
    def conversionMass(self, number, value_1, value_2):
        # проверка полей ввода
        if number == "":
            self.showEmptyError()
        elif number.isalpha():
            self.showStrError()
        else:
            num = float(number)
            if value_1 == "Килограмм" and value_2 == "Грамм":
                rez1 = num * 1000
                rez2 = num / 1000
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))
            elif value_1 == "Центнер" and value_2 == "Килограмм":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))
            elif value_1 == "Центнер" and value_2 == "Грамм":
                rez1 = num * 100000
                rez2 = num / 100000
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))
            elif value_1 == "Тонна" and value_2 == "Килограмм":
                rez1 = num * 1000
                rez2 = num / 1000
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))
            elif value_1 == "Тонна" and value_2 == "Центнер":
                rez1 = num * 10
                rez2 = num / 10
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))
            elif value_1 == "Тонна" and value_2 == "Грамм":
                rez1 = num * 1000000
                rez2 = num / 1000000
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))
            elif value_1 == "Килограмм" and value_2 == "Тонна":
                rez1 = num * 0.001
                rez2 = num / 0.001
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))
            elif value_1 == "Грамм" and value_2 == "Тонна":
                rez1 = num * 1000000
                rez2 = num / 1000000
                self.ui.lbl_rezult_conversion_5.setText(str(rez1))
                self.ui.lbl_rezult_conversion_6.setText(str(rez2))

    # перевод единиц времени
    def conversionTime(self, number, value_1, value_2):
        # проверка полей ввода
        if number == "":
            self.showEmptyError()
        elif number.isalpha():
            self.showStrError()
        else:
            num = float(number)
            if value_1 == "Минута" and value_2 == "Секунда":
                rez1 = num * 60
                rez2 = num / 60
                self.ui.lbl_rezult_conversion_7.setText(str(rez1))
                self.ui.lbl_rezult_conversion_8.setText(str(rez2))
            elif value_1 == "Час" and value_2 == "Минута":
                rez1 = num * 60
                rez2 = num / 60
                self.ui.lbl_rezult_conversion_7.setText(str(rez1))
                self.ui.lbl_rezult_conversion_8.setText(str(rez2))
            elif value_1 == "Час" and value_2 == "Секунда":
                rez1 = num * 3600
                rez2 = num / 3600
                self.ui.lbl_rezult_conversion_7.setText(str(rez1))
                self.ui.lbl_rezult_conversion_8.setText(str(rez2))
            elif value_1 == "Сутки" and value_2 == "Час":
                rez1 = num * 24
                rez2 = num / 24
                self.ui.lbl_rezult_conversion_7.setText(str(rez1))
                self.ui.lbl_rezult_conversion_8.setText(str(rez2))
            elif value_1 == "Год" and value_2 == "Месяц":
                rez1 = num * 12
                rez2 = num / 12
                self.ui.lbl_rezult_conversion_7.setText(str(rez1))
                self.ui.lbl_rezult_conversion_8.setText(str(rez2))
            elif value_1 == "Век" and value_2 == "Лет":
                rez1 = num * 100
                rez2 = num / 100
                self.ui.lbl_rezult_conversion_7.setText(str(rez1))
                self.ui.lbl_rezult_conversion_8.setText(str(rez2))

    # функции калькулятора
    def getValues(self, value):
        # получаем числа
        oldValue = self.ui.lbl_calc_rez.text()
        # сохраняем результаты в переменную
        rez = "%s%s" % (str(oldValue), str(value))
        # вставляем число в лейбл
        self.ui.lbl_calc_rez.setText(rez.strip())
        # возвращаем эту запись
        return rez

    def insertRez(self):
        # переменная, хранаящая результат функции
        action = self.getValues("")
        # блок проверки деления на ноль
        try:
            # счёт записи, возвращённой функцией
            rez = str(eval(str(action)))
            # вставляем результат в лейбл
            self.ui.lbl_calc_rez.setText(rez)
            # история действий
            # действия
            actions = f"{action}={rez}"
            # предыдущие действия
            oldAction = self.ui.pte_history.toPlainText()
            history = "%s%s\n" % (str(oldAction), str(actions))
            # вставляем историю действия в текстовое поле
            self.ui.pte_history.setPlainText(history)
        except ZeroDivisionError:
            sign = ["∞", "ERROR"]
            self.ui.lbl_calc_rez.setText(random.choice(sign))
        except ValueError:
            self.ui.lbl_calc_rez.setText("ERROR")
        except TypeError:
            self.ui.lbl_calc_rez.setText("ERROR")

    def count_sqrt(self):
        try:
            # получаем значение из лейбла
            value = self.ui.lbl_calc_rez.text()
            # считаем значение из лейбла
            rez_from_lbl = int(eval(value))
            # считаем квадратный корень из получившегося значения
            sqrt_rez = math.sqrt(rez_from_lbl)
            # вставляем полученное значение в лейбл
            self.ui.lbl_calc_rez.setText(str(sqrt_rez))
            # история действий
            actions = f"√{value} = {sqrt_rez}"
            oldAction = self.ui.pte_history.toPlainText()
            history = "%s%s\n" % (str(oldAction), str(actions))
            # вставляем историю действия в текстовое поле
            self.ui.pte_history.setPlainText(history)
        except ValueError:
            self.ui.lbl_calc_rez.setText("ERROR")

    def count_sin(self):
        # список углов
        corner_dict = {"0": "0", "30": "0.5", "45": "0.70", "60": "0.86", "90": "1", "120": "0.86", "135": "0.70",
                       "150": "0.5", "180": "0", "210": "-0.5", "225": "-0.70", "240": "-0.86", "270": "-1",
                       "300": "-0.86", "315": "-0.70", "330": "-0.5", "360": "0"}
        # получаем текст из лейбла
        lbl_rez = self.ui.lbl_calc_rez.text()

        for key, value in corner_dict.items():
            if key == lbl_rez:
                actions = f"sin {key} = {value}"
                # вставляем предыдущее действие в текстовое поле
                oldAction = self.ui.pte_history.toPlainText()
                history = "%s%s\n" % (str(oldAction), str(actions))
                # вставляем историю действия в текстовое поле
                self.ui.pte_history.setPlainText(history)
                # вставляем результат в лейбл
                self.ui.lbl_calc_rez.setText(value)

    def count_cos(self):
        corner_dict = {"0": "1", "30": "0.86", "45": "0.70", "60": "0.5", "90": "0", "120": "-0.5", "135": "-0.86",
                       "150": "-0.70", "180": "-1", "210": "-0.86", "225": "-0.70", "240": "-0.5", "270": "0",
                       "300": "0.5", "315": "0.70", "330": "0.86", "306": "1"}

        lbl_rez = self.ui.lbl_calc_rez.text()
        for key, value in corner_dict.items():
            if key == lbl_rez:
                actions = f"sin {key} = {value}"
                oldAction = self.ui.pte_history.toPlainText()
                history = "%s%s\n" % (str(oldAction), str(actions))
                # вставляем историю действия в текстовое поле
                self.ui.pte_history.setPlainText(history)
                # вставляем результат в лейбл
                self.ui.lbl_calc_rez.setText(value)

    def count_tg(self):
        corner_dict = {"0": "0", "30": "0.57", "45": "1", "60": "1.73", "90": "_", "120": "-1.73", "135": "-1",
                       "150": "-0.57",
                       "180": "0", "210": "0.57", "225": "1", "240": "1.73", "270": "_", "300": "-1.73", "315": "-1",
                       "330": "0.57", "360": "0"}

        lbl_rez = self.ui.lbl_calc_rez.text()
        for key, value in corner_dict.items():
            if key == lbl_rez:
                actions = f"sin {key} = {value}"
                oldAction = self.ui.pte_history.toPlainText()
                history = "%s%s\n" % (str(oldAction), str(actions))
                # вставляем историю действия в текстовое поле
                self.ui.pte_history.setPlainText(history)
                # вставляем результат в лейбл
                self.ui.lbl_calc_rez.setText(value)

    def count_ctg(self):
        corner_dict = {"0": "_", "30": "1.73", "45": "1", "60": "0.57", "90": "0", "120": "-0.57", "135": "-1",
                       "150": "-1.73",
                       "180": "_", "210": "1.73", "225": "1", "240": "0.57", "270": "0", "300": "-0.57", "315": "-1",
                       "330": "1.73", "360": "_"}
        lbl_rez = self.ui.lbl_calc_rez.text()
        for key, value in corner_dict.items():
            if key == lbl_rez:
                actions = f"sin {key} = {value}"
                oldAction = self.ui.pte_history.toPlainText()
                history = "%s%s\n" % (str(oldAction), str(actions))
                # вставляем историю действия в текстовое поле
                self.ui.pte_history.setPlainText(history)
                # вставляем результат в лейбл
                self.ui.lbl_calc_rez.setText(value)

