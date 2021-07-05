from PyQt5.QtWidgets import QMessageBox
from main_ui import Ui_MainWindow
import re
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
            self.countPa(self.ui.le_get_data.text())
        elif value == "кПа":
            self.countkPa(self.ui.le_get_data.text())
        elif value == "МПа":
            self.countMPA(self.ui.le_get_data.text())
        elif value == "кГс/см2":
            self.countkGs(self.ui.le_get_data.text())
        elif value == "физ.атм":
            self.countfizatm(self.ui.le_get_data.text())
        elif value == "мм.рт.ст":
            self.countmmrtst(self.ui.le_get_data.text())
        elif value == "мм.вод.ст":
            self.countmmvodst(self.ui.le_get_data.text())
        elif value == "bar":
            self.countbar(self.ui.le_get_data.text())
        elif value == "psi":
            self.countpsi(self.ui.le_get_data.text())

    # счёт па
    def countPa(self, value):
        # проверка поля ввода
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # па
            rez_pa = num
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 0.001
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.000001
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/СМ2
            rez_kGs = num * 0.0000102
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.атм
            rez_fiz = num * 0.00000987
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 0.0075006
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст.
            rez_mm_vod_st = num * 0.101972
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 0.00001
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 0.00014504
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    def countkPa(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 1000
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.001
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num * 0.0101972
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.фтм.
            rez_fiz = num * 0.00986923
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 7.50062
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст
            rez_mm_vod_st = num * 101.9716
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 0.01
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 0.1450377
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    def countMPA(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 10000000
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 1000
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num * 10.19716
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.фтм.
            rez_fiz = num * 9.86923
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 7500.62
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст
            rez_mm_vod_st = num * 101971.6
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 10
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 145.0377
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    # чёт кГс/см2
    def countkGs(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 98066.5
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 98.0665
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.0980665
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.атм
            rez_fiz = num * 0.967841
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 735.559
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст.
            rez_mm_vod_st = num * 100000
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 0.980665
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 14.223344
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    # счёт физ.атм.
    def countfizatm(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 101325
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 101.325
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.101325
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num * 1.033227
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.атм
            rez_fiz = num
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 760
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст.
            rez_mm_vod_st = num * 10332.27
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 1.01325
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 14.6959
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    def countmmrtst(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 133.3224
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 0.1333224
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.00011333
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num * 0.0013595
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.атм
            rez_fiz = num * 0.00131579
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст.
            rez_mm_vod_st = num * 13.6
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 0.00133322
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 0.019336
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    # счёт мм.вод.ст.
    def countmmvodst(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 9.80665
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 0.00980665
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.00000981
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num * 0.0001
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.атм
            rez_fiz = num * 0.00009678
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 0.073556
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст.
            rez_mm_vod_st = num
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 0.00009807
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 0.00142233
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    # счёт bar
    def countbar(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 100000
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 100
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.1
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num * 1.019716
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.атм
            rez_fiz = num * 0.986923
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 750.062
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст.
            rez_mm_vod_st = num * 10197.16
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num * 14.50377
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

    def countpsi(self, value):
        if value == "":
            self.showEmptyError()
        elif value.isalpha():
            self.showStrError()
        else:
            num = float(value)
            # Па
            rez_pa = num * 6894.757
            self.ui.lbl_rez_1.setText(str(round(rez_pa, 2)))
            # кПа
            rez_kPa = num * 6.894757
            self.ui.lbl_rez_2.setText(str(round(rez_kPa, 2)))
            # МПа
            rez_MPa = num * 0.006894756
            self.ui.lbl_rez_3.setText(str(round(rez_MPa, 2)))
            # кГс/см2
            rez_kGs = num * 0.070307
            self.ui.lbl_rez_4.setText(str(round(rez_kGs, 2)))
            # физ.атм
            rez_fiz = num * 0.068046
            self.ui.lbl_rez_5.setText(str(round(rez_fiz, 2)))
            # мм.рт.ст.
            rez_mm_rt_st = num * 51.715217
            self.ui.lbl_rez_6.setText(str(round(rez_mm_rt_st, 2)))
            # мм.вод.ст.
            rez_mm_vod_st = num * 703.07
            self.ui.lbl_rez_7.setText(str(round(rez_mm_vod_st, 2)))
            # bar
            rez_bar = num * 0.0689476
            self.ui.lbl_rez_8.setText(str(round(rez_bar, 2)))
            # psi
            rez_psi = num
            self.ui.lbl_rez_9.setText(str(round(rez_psi, 2)))

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
