import json

BTN_COLORS_FILE_JSON = "btn_colors.json"

class Save:
    # ��������� ����� ������� ����
    def get_color_from_cb(self, *args, cb_colors):
        # cb_colors - ���� �� ����������� ������
        # *args - ������ ������� � ����������, � ������� ����� �������� ����
        global value
        try:
            with open("colors_config.json", "r") as file:
                colors = json.load(file)
                # color = self.ui.cb_bg_colors.currentText()
                color = cb_colors.currentText() # �������� ���� �� ����������� ������
                for key, value in colors.items():
                    if key == color: # ���� �������� ����� ��������� �� json ����� ��������� � ��������� ����� �� ����������� ������
                        # self.ui.fr_settings.setStyleSheet(value)
                        for items in args:
                            for bg in items:
                                bg.setStyleSheet(value) # ������������� �������� �� �����
                            return value
        except FileExistsError():
            pass

    # ��������� ��������� ����
    def save_the_selected_color(self):
        try:
            with open("bg_color.json", "w", encoding="utf-8") as file:
                res = {"bg_color": value}
                json.dump(res, file, ensure_ascii=False)
        except FileExistsError():
            pass

    def save_the_selected_txt_color(self):
        try:
            with open("label_txt_color.json", "w", encoding="utf-8") as file_2:
                res_2 = {"lbl_txt_color": value}
                json.dump(res_2, file_2, ensure_ascii=False)
        except FileExistsError():
            pass

    # ��������� ���������
    def load_settings(self, *args):
        try:
            with open("bg_color.json", "r") as file:
                rez = json.load(file)
                for items in args:
                    for bg in items:
                        if len(rez) > 0:
                            bg.setStyleSheet(rez["bg_color"])
                            # return rez["bg_color"]
                        else:
                            bg.setStyleSheet("background-color: #222831;")
        except FileExistsError():
            pass

    # ���������� ���������� ���������
    def reset_saved_settings(self):
        pass