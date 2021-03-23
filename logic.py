from PyQt5 import QtWidgets, QtGui, QtCore
from main_ui import Ui_MainWindow


class Calculator:
    ui = Ui_MainWindow()

    def getLength(self, value_1, value_2, number_1, number_2):
        num_1 = int(number_1)
        num_2 = int(number_2)
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

    def getMass(self, value_1, value_2, number_1, number_2):
        num_1 = int(number_1)
        num_2 = int(number_2)
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

    def getSquare(self, value_1, value_2, number_1, number_2):
        num_1 = int(number_1)
        num_2 = int(number_2)
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

    def getTime(self, value_1, value_2, number_1, number_2):
        num_1 = int(number_1)
        num_2 = int(number_2)
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
        num = int(value)
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
        # Па
        num = float(value)
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
