from interface import LoardingScreen
import sys
from PyQt5 import QtWidgets


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = LoardingScreen()
    application.show()
    sys.exit(app.exec_())


# pyuic5 UI/progressbar_ui.ui -o progressbar_ui.py
# pyuic5 UI/exit_window_ui.ui -o exit_window_ui.py
# pyuic5 UI/main_ui.ui -o main_ui.py

# pyinstaller -w --onefile -i "C:\PycharmProjects\ConverterSize\resources/icon.ico" main.py
# pyinstaller -w --onefile --icon=icon.ico main.py
# pyinstaller -w -F -i "icon.ico" main.py
# pyinstaller --onefile --icon=resources/icon.ico --noconsole main.py
# pyinstaller main.spec
# self.btn_unit_converter
# pyinstaller --onefile --icon=C:\PycharmProjects\ConverterSize\resources/icon.ico --noconsole main.py

