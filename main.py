import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogContentContainer,
)
from kivymd.uix.divider import MDDivider
from kivymd.uix.list import (
    MDListItem,
    MDListItemSupportingText,
)

Window.size = (355,655)

data_list=[]
counter_1 = 0
counter_2 = 0
counter_3 = 0
counter_4 = 0
counter_5 = 0

data = "database.json"

try:
    with open(data) as file:
        data = json.load(file)
        print("Файл открылся")
except (FileNotFoundError, json.decoder.JSONDecodeError):
    with open(data, "w", encoding='utf-8') as file:
        json.dump({
    "Ученик №1": "пусто",
    "Ученик №2": "пусто",
    "Ученик №3": "пусто",
    "Ученик №4": "пусто",
    "Ученик №5": "пусто",
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0
}, file)
    print("Файл создался")
    with open(data) as file:
        data = json.load(file)

class MDSM(MDScreenManager):
    pass

class Screen_1(MDScreen):
    pass

class Screen_2(MDScreen):

    hint = "         Инструкция \nДля начала во вкладке\n         (Моя группа) необходимо \
добавить фамилию и имя студентов.\nПосле нажать на кнопку обновить, \
студенты появятся в списке. Снизу студента указана 'Количество \
пропусков', а справа счетик Н. При нажатии на счетчик - будет \
записываться количество пропусков.\nЕсли есть данные в БД, необходимо нажать на обновить!"

    def counter1(self):
        global counter_1, data
        counter_1 += 1
        self.ids.c1.text = str(counter_1)
        data["1"] = counter_1
        with open("database.json", "w") as file:
            json.dump(data , file,  indent=4, ensure_ascii=False)
    
    def counter2(self):
        global counter_2
        counter_2 += 1
        self.ids.c2.text = str(counter_2)
        data["2"] = counter_2
        with open("database.json", "w") as file:
            json.dump(data , file,  indent=4, ensure_ascii=False)
    
    def counter3(self):
        global counter_3
        counter_3 += 1
        self.ids.c3.text = str(counter_3)
        data["3"] = counter_3
        with open("database.json", "w") as file:
            json.dump(data , file,  indent=4, ensure_ascii=False)

    def counter4(self):
        global counter_4
        counter_4 += 1
        self.ids.c4.text = str(counter_4)
        data["4"] = counter_4
        with open("database.json", "w") as file:
            json.dump(data , file,  indent=4, ensure_ascii=False)

    def counter5(self):
        global counter_5
        counter_5 += 1
        self.ids.c5.text = str(counter_5)
        data["5"] = counter_5
        with open("database.json", "w") as file:
            json.dump(data , file,  indent=4, ensure_ascii=False)

    def refresh(self):
        global data, counter_1, counter_2, counter_3, counter_4, counter_5
        self.ids.c1.text = str(data["1"])
        self.ids.c2.text = str(data["2"])
        self.ids.c3.text = str(data["3"])
        self.ids.c4.text = str(data["4"])
        self.ids.c5.text = str(data["5"])
        counter_1 = data["1"]
        counter_2 = data["2"]
        counter_3 = data["3"]
        counter_4 = data["4"]
        counter_5 = data["5"]
        x = self.manager.get_screen("Screen_3")
        if data["Ученик №1"] != "пусто": self.ids.n1n.text = data["Ученик №1"]
        else: self.ids.n1n.text = x.ids.n1.text
        if data["Ученик №2"] != "пусто": self.ids.n2n.text = data["Ученик №2"]
        else: self.ids.n2n.text = x.ids.n2.text
        if data["Ученик №3"] != "пусто": self.ids.n3n.text = data["Ученик №3"]
        else: self.ids.n3n.text = x.ids.n3.text
        if data["Ученик №4"] != "пусто": self.ids.n4n.text = data["Ученик №4"]
        else: self.ids.n4n.text = x.ids.n4.text
        if data["Ученик №5"] != "пусто": self.ids.n5n.text = data["Ученик №5"]
        else: self.ids.n5n.text = x.ids.n5.text
    
class Screen_3(MDScreen):

    hint = "         Инструкция \nДля начала необходимо указать фамилию и имя студента. \
После нажать на кнопку добавить. Студент появится в списке. \nПри необходимости можно \
удалить студента. Удаляется последний студент снизу!\n\
Если есть данные в БД, необходимо нажать на обновить!"

    def refdata(self):
        global data
        if data["Ученик №1"] != "пусто": self.ids.n1.text = data["Ученик №1"]
        if data["Ученик №2"] != "пусто": self.ids.n2.text = data["Ученик №2"]
        if data["Ученик №3"] != "пусто": self.ids.n3.text = data["Ученик №3"]
        if data["Ученик №4"] != "пусто": self.ids.n4.text = data["Ученик №4"]
        if data["Ученик №5"] != "пусто": self.ids.n5.text = data["Ученик №5"]
    
    def delete_data(self):
        global data_list, data, t1, t2, t3, t4, t5
        if data["Ученик №5"] != "пусто":
            data["Ученик №5"] = "пусто"
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №4"] != "пусто":
            data["Ученик №4"] = "пусто"
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №3"] != "пусто":
            data["Ученик №3"] = "пусто"
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №2"] != "пусто":
            data["Ученик №2"] = "пусто"
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №1"] != "пусто":
            data["Ученик №1"] = "пусто"
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        if self.ids.n5.text != ">Ученик №5": self.ids.n5.text = ">Ученик №5"
        elif self.ids.n4.text != ">Ученик №4": self.ids.n4.text = ">Ученик №4"
        elif self.ids.n3.text != ">Ученик №3": self.ids.n3.text = ">Ученик №3"
        elif self.ids.n2.text != ">Ученик №2": self.ids.n2.text = ">Ученик №2"
        elif self.ids.n1.text != ">Ученик №1": self.ids.n1.text = ">Ученик №1"

    def save_data(self):
        global data_list, data
        name = self.ids.name_input.text
        surname = self.ids.surname_input.text
        data_list.append(f'{surname} {name}')
        if data["Ученик №1"] == "пусто":
            data["Ученик №1"] = f'{surname} {name}'
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №2"] == "пусто":
            data["Ученик №2"] = f'{surname} {name}'
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №3"] == "пусто":
            data["Ученик №3"] = f'{surname} {name}'
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №4"] == "пусто":
            data["Ученик №4"] = f'{surname} {name}'
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        elif data["Ученик №5"] == "пусто":
            data["Ученик №5"] = f'{surname} {name}'
            with open("database.json", "w") as file:
                json.dump(data , file,  indent=4, ensure_ascii=False)
        if self.ids.n1.text == ">Ученик №1": self.ids.n1.text = f'{surname} {name}'
        elif self.ids.n2.text == ">Ученик №2": self.ids.n2.text = f'{surname} {name}'
        elif self.ids.n3.text == ">Ученик №3": self.ids.n3.text = f'{surname} {name}'
        elif self.ids.n4.text == ">Ученик №4": self.ids.n4.text = f'{surname} {name}'
        elif self.ids.n5.text == ">Ученик №5": self.ids.n5.text = f'{surname} {name}'
        self.ids.name_input.text = ""
        self.ids.surname_input.text = ""

class Screen_4(MDScreen):

    def show_alert_dialog(self):
        global counter_1, counter_2, counter_3, counter_4, counter_5
        a1,a2,a3,a4, a5 = "","","","",""
        x = self.manager.get_screen("Screen_3")
        a1 = x.ids.n1.text
        a2 = x.ids.n2.text
        a3 = x.ids.n3.text
        a4 = x.ids.n4.text
        a5 = x.ids.n5.text
        MDDialog(
            # ----------------------------Icon-----------------------------
            MDDialogIcon(
                icon="file-outline",
            ),
            # -----------------------Headline text-------------------------
            MDDialogHeadlineText(
                text="Отчет",
            ),
            # -----------------------Supporting text-----------------------
            MDDialogSupportingText(
                text="Отчет о посещаемости студентов:",
            ),
            # -----------------------Custom content------------------------
            MDDialogContentContainer(
                MDDivider(),
                MDListItem(
                    MDListItemSupportingText(
                        text=f"{a1} Кол-во Н = {counter_1}",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                MDListItem(
                    MDListItemSupportingText(
                        text=f"{a2} Кол-во Н = {counter_2}",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                MDListItem(
                    MDListItemSupportingText(
                        text=f"{a3} Кол-во Н = {counter_3}",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                MDListItem(
                    MDListItemSupportingText(
                        text=f"{a4} Кол-во Н = {counter_4}",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                MDListItem(
                    MDListItemSupportingText(
                        text=f"{a5} Кол-во Н = {counter_5}",
                    ),
                    theme_bg_color="Custom",
                    md_bg_color=self.theme_cls.transparentColor,
                ),
                MDDivider(),
                orientation="vertical",
            ),
        ).open()

    def clear_count(self):
        global counter_1, counter_2, counter_3, counter_4, counter_5
        counter_1 = counter_2 = counter_3 = counter_4 = counter_5 = 0
        x = self.manager.get_screen("Screen_2")
        x.ids.c1.text = str(counter_1)
        x.ids.c2.text = str(counter_2)
        x.ids.c3.text = str(counter_3)
        x.ids.c4.text = str(counter_4)
        x.ids.c5.text = str(counter_5)
        data["1"] = counter_1
        data["2"] = counter_2
        data["3"] = counter_3
        data["4"] = counter_4
        data["5"] = counter_5
        with open("database.json", "w") as file:
            json.dump(data , file,  indent=4, ensure_ascii=False)

class MyApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.title = "Журнал"
        kv = Builder.load_file("layout.kv")
        return kv 
    
    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "White" if self.theme_cls.primary_palette == "Blue" else "Blue"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )

    def exit_app(self):
        self.stop()

if __name__ == '__main__':
    MyApp().run()
