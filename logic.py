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
