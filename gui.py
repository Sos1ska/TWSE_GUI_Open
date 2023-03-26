from json import load   # Парсинг данных из кэша
from modules.logger import log_start, log_start_with_arg   # Лог запуска модулей
from modules.__ip__ import ip as ip_module   # Важные модули
from modules.__mac__ import mac as mac_module
from modules.__number__ import number as number_module
from os import path as folder   # Понимать в какой среде работаем
from os import mkdir   # Создание папки, если нету
from tkinter import *   # Сам движок
from tkinter import ttk
from tkinter import messagebox
global path

def os(_path):   # Нужен чтобы понимать, что за ОС ну и правильные пути к папкам в ОС
    import os
    if os.sys.platform == "win32" : _path = _path.replace("/", "\\")
    else : _path = _path.replace("\\", "/")
    return _path

path = folder.abspath("work")   # Получить саму рабочаю область

if "work" in path : path=path.replace(r"work", "")
else: 
    if "work" in path : path=path.replace(r"work", "")
if folder.exists(os(path+"cache")) == True : pass
else : mkdir(os(path+"cache"))

class config:   # Настройки
    with open(os(path+"config/system.json"), "r") as file_config_load : config = load(file_config_load)

def _ip():  # Метод получения и обработки IP-Адреса
    _local_ip = _gui().IPEntry.get()
    @log_start_with_arg("_ip.__main__", _local_ip)
    def __main__(ip):
        ip_module(ip, config.config["Main"]["Proxy"])
        match folder.exists(os(path+"cache/answer.json.ip")):
            case True:
                with open(os(path+"cache/answer.json.ip"), "r") as file_in_cache_answer : Handler_answer = load(file_in_cache_answer)
                match Handler_answer["Answer"]:
                    case "200":
                        _second_gui_answer().answer_gui("ip")
                    case "503":
                        messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error code \"503\"")
                    case "424":
                        messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error code \"424\"")
            case False:
                messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error with work files")
def _mac():    # Метод получения и обработки MAC-Адреса
    _local_mac = _gui().MACEntry.get()
    @log_start_with_arg("_mac.__main__", _local_mac)
    def __main__(mac):
        mac_module(mac, config.config["Main"]["Proxy"])
        match folder.exists(os(path+"cache/answer.json.mac")):
            case True:
                with open(os(path+"cache/answer.json.mac"), "r") as file_in_cache_answer : Handler_answer = load(file_in_cache_answer)
                match Handler_answer["Answer"]:
                    case "200":
                        _second_gui_answer().answer_gui("mac")
                    case "503":
                        messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error code \"503\"")
                    case "424":
                        messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error code \"424\"")
            case False:
                messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error with work files")
def _number():    # Метод получения и обработки номера телефона
    _local_number = _gui().NumberEntry.get()
    @log_start_with_arg("_number.__main__", _local_number)
    def __main__(number):
        number_module(number, False)
        match folder.exists(os(path+"cache/answer.json.number")):
            case True:
                with open(os(path+"cache/answer.json.number"), "r") as file_in_cache_answer : Handler_answer = load(file_in_cache_answer)
                match Handler_answer["Answer"]:
                    case "200":
                        _second_gui_answer().answer_gui("number")
                    case "503":
                        messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error code \"503\"")
                    case "424":
                        messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error code \"424\"")
            case False:
                messagebox.showerror(config.config["Main"]["_Notification"]["_Title"], "Error with work files")

def _quit():    # Модуль для выхода из ПО
    @log_start("_quit.__main__")
    def __main__():
        quit()

class _gui:    # Главный класс, который создаёт окно для пользователя
    Main = Tk()    # Корень главного окна
    config = config.config    # Получение настроек из класса config
    IPEntry = Entry(Main)   # Поле для IP-Адреса
    MACEntry = Entry(Main)   # Поле для MAC-Адреса
    NumberEntry = Entry(Main)   # Поле для номера телефона
    IPButton = ttk.Button(Main, text="Break", command=_ip)   # Ну тут логично. Кнопки
    MACButton = ttk.Button(Main, text="Break", command=_mac)
    NumberButton = ttk.Button(Main, text="Break", command=_number)
    Quit = ttk.Button(Main, text="Exit", command=_quit)
    def gui(self):   # Создание окна
        @log_start("_gui.gui.__main__")
        def __main__():
            self.Main.title(self.config["Main"]["_Title"])
            geometry_x = self.config["Main"]["_Screen"]["x"]
            geometry_y = self.config["Main"]["_Screen"]["y"]
            self.Main.geometry(f"{geometry_x}x{geometry_y}")
            self.Main.resizable(False, False)
            self.Main.iconbitmap(os(path+self.config["Main"]["_Ico"]))
            self._labels()
            self._entrys()
            self._buttons()
        self.Main.mainloop()
    def _labels(self):   # Создание текста
        @log_start("_gui._label.__main__")
        def __main__():
            IP = Label(self.Main, text="IP-Address", font=("", 15))
            MAC = Label(self.Main, text="MAC-Address", font=("", 15))
            Number = Label(self.Main, text="NumberPhone", font=("", 15))
            IP.place(relx=self.config["Main"]["_Locations"]["_Labels"]["IP"]["x"], rely=self.config["Main"]["_Locations"]["_Labels"]["IP"]["y"])
            MAC.place(relx=self.config["Main"]["_Locations"]["_Labels"]["MAC"]["x"], rely=self.config["Main"]["_Locations"]["_Labels"]["MAC"]["y"])
            Number.place(relx=self.config["Main"]["_Locations"]["_Labels"]["Number"]["x"], rely=self.config["Main"]["_Locations"]["_Labels"]["Number"]["y"])
    def _entrys(self):   # Создание полей для ввода
        @log_start("_gui._entrys.__main__")
        def __main__():
            self.IPEntry.place(relx=self.config["Main"]["_Locations"]["_Entrys"]["IP"]["x"], rely=self.config["Main"]["_Locations"]["_Entrys"]["IP"]["y"])
            self.MACEntry.place(relx=self.config["Main"]["_Locations"]["_Entrys"]["MAC"]["x"], rely=self.config["Main"]["_Locations"]["_Entrys"]["MAC"]["y"])
            self.NumberEntry.place(relx=self.config["Main"]["_Locations"]["_Entrys"]["Number"]["x"], rely=self.config["Main"]["_Locations"]["_Entrys"]["Number"]["y"])
    def _buttons(self):   # Создание кнопок
        @log_start("_gui._buttons.__main__")
        def __main__():
            self.IPButton.place(relx=self.config["Main"]["_Locations"]["_Buttons"]["IP"]["x"], rely=self.config["Main"]["_Locations"]["_Buttons"]["IP"]["y"])
            self.MACButton.place(relx=self.config["Main"]["_Locations"]["_Buttons"]["MAC"]["x"], rely=self.config["Main"]["_Locations"]["_Buttons"]["MAC"]["y"])
            self.NumberButton.place(relx=self.config["Main"]["_Locations"]["_Buttons"]["Number"]["x"], rely=self.config["Main"]["_Locations"]["_Buttons"]["Number"]["y"])
            self.Quit.place(relx=self.config["Main"]["_Locations"]["_Buttons"]["Quit"]["x"], rely=self.config["Main"]["_Locations"]["_Buttons"]["Quit"]["y"])

class _second_gui_answer:   # "Подручный класс". Я считаю его подручным, т.к. он создаёт нам уже окно ответа
    def answer_gui(self, _method):   # Создание окна
        Main = Tk()
        second_config = _gui.config
        @log_start_with_arg("_second_gui_answer.answer_gui.__main__", _method)
        def __main__(_method):
            match _method:   # Парсим метод
                case "ip":   # Для IP-Адреса
                    with open(os(path+"cache/ip.json"), "r") as file_in_cache_with_data : upload = load(file_in_cache_with_data)
                    Main.title(second_config["AnswerIP"]["_Title"])
                    geometry_x = second_config["AnswerIP"]["_Screen"]["x"]
                    geometry_y = second_config["AnswerIP"]["_Screen"]["y"]
                    Main.geometry(f"{geometry_x}x{geometry_y}")
                    Main.resizable(False, False)
                    Main.iconbitmap(os(path+second_config["AnswerIP"]["_Ico"]))
                    try:
                        Continent = Label(Main, text=upload["Continent"])
                        Country = Label(Main, text=upload["Country"])
                        RegionName = Label(Main, text=upload["regionName"])
                        City = Label(Main, text=upload["City"])
                        Lat = Label(Main, text=upload["Lat"])
                        Lon = Label(Main, text=upload["Lon"])
                        ISP = Label(Main, text=upload["ISP"])
                        ORG = Label(Main, text=upload["ORG"])
                        AS = Label(Main, text=upload["AS"])
                        ASName = Label(Main, text=upload["ASName"])
                        Reverse = Label(Main, text=upload["Reverse"])
                    except Exception as ex : messagebox.showerror(second_config["Main"]["_Notification"]["_Title"], ex)
                    finally:
                        Continent.place(relx=second_config["AnswerIP"]["_Locations"]["Continent"]["x"], rely=second_config["AnswerIP"]["_Locations"]["Continent"]["y"])
                        Country.place(relx=second_config["AnswerIP"]["_Locations"]["Country"]["x"], rely=second_config["AnswerIP"]["_Locations"]["Country"]["y"])
                        RegionName.place(relx=second_config["AnswerIP"]["_Locations"]["RegionName"]["x"], rely=second_config["AnswerIP"]["_Locations"]["RegionName"]["y"])
                        City.place(relx=second_config["AnswerIP"]["_Locations"]["City"]["x"], rely=second_config["AnswerIP"]["_Locations"]["City"]["y"])
                        Lat.place(relx=second_config["AnswerIP"]["_Locations"]["Lat"]["x"], rely=second_config["AnswerIP"]["_Locations"]["Lat"]["y"])
                        Lon.place(relx=second_config["AnswerIP"]["_Locations"]["Lon"]["x"], rely=second_config["AnswerIP"]["_Locations"]["Lon"]["y"])
                        ISP.place(relx=second_config["AnswerIP"]["_Locations"]["ISP"]["x"], rely=second_config["AnswerIP"]["_Locations"]["ISP"]["y"])
                        ORG.place(relx=second_config["AnswerIP"]["_Locations"]["ORG"]["x"], rely=second_config["AnswerIP"]["_Locations"]["ORG"]["y"])
                        AS.place(relx=second_config["AnswerIP"]["_Locations"]["AS"]["x"], rely=second_config["AnswerIP"]["_Locations"]["AS"]["y"])
                        ASName.place(relx=second_config["AnswerIP"]["_Locations"]["ASName"]["x"], rely=second_config["AnswerIP"]["_Locations"]["ASName"]["y"])
                        Reverse.place(relx=second_config["AnswerIP"]["_Locations"]["Reverse"]["x"], rely=second_config["AnswerIP"]["_Locations"]["Reverse"]["y"])
                        Main.mainloop()
                case "mac":   # Для MAC-Адреса
                    with open(os(path+"cache/mac.json"), "r") as file_in_cache_with_data : upload = load(file_in_cache_with_data)
                    Main.title(second_config["AnswerMAC"]["_Title"])
                    geometry_x = second_config["AnswerMAC"]["_Screen"]["x"]
                    geometry_y = second_config["AnswerMAC"]["_Screen"]["y"]
                    Main.geometry(f"{geometry_x}x{geometry_y}")
                    Main.resizable(False, False)
                    Main.iconbitmap(os(path+second_config["AnswerMAC"]["_Ico"]))
                    try:
                        Company = Label(Main, text=upload["Company"])
                        Address = Label(Main, text=upload["Address"])
                        Block_Size = Label(Main, text=upload["Block_Size"])
                    except Exception as ex : messagebox.showerror(second_config["Main"]["_Notification"]["_Title"], ex)
                    finally:
                        Company.place(relx=second_config["AnswerMAC"]["_Locations"]["Company"]["x"], rely=second_config["AnswerMAC"]["_Locations"]["Company"]["y"])
                        Address.place(relx=second_config["AnswerMAC"]["_Locations"]["Address"]["x"], rely=second_config["AnswerMAC"]["_Locations"]["Address"]["y"])
                        Block_Size.place(relx=second_config["AnswerMAC"]["_Locations"]["Block_Size"]["x"], rely=second_config["AnswerMAC"]["_Locations"]["Block_Size"]["y"])
                case "number":   # Для номера телефона
                    with open(os(path+"cache/number.json"), "r") as file_in_cache_with_data : upload = load(file_in_cache_with_data)
                    Main.title(second_config["AnswerNumber"]["_Title"])
                    geometry_x = second_config["AnswerNumber"]["_Screen"]["x"]
                    geometry_y = second_config["AnswerNumber"]["_Screen"]["y"]
                    Main.geometry(f"{geometry_x}x{geometry_y}")
                    Main.resizable(False, False)
                    Main.iconbitmap(os(path+second_config["AnswerNumber"]["_Ico"]))
                    try:
                        OperName = Label(Main, text=upload["OperName"])
                        OperMNC = Label(Main, text=upload["OperMNC"])
                        OperBrand = Label(Main, text=upload["OperBrand"])
                        OperINN = Label(Main, text=upload["OperINN"])
                        RegionNames = Label(Main, text=upload["RegionName"])
                    except Exception as ex : messagebox.showerror(second_config["Main"]["_Notification"]["_Title"], ex) 
                    finally:
                        OperName.place(relx=second_config["AnswerNumber"]["_Locations"]["OperName"]["x"], rely=second_config["AnswerNumber"]["_Locations"]["OperName"]["y"])
                        OperMNC.place(relx=second_config["AnswerNumber"]["_Locations"]["OperMNC"]["x"], rely=second_config["AnswerNumber"]["_Locations"]["OperMNC"]["y"])
                        OperBrand.place(relx=second_config["AnswerNumber"]["_Locations"]["OperBrand"]["x"], rely=second_config["AnswerNumber"]["_Locations"]["OperBrand"]["y"])
                        OperINN.place(relx=second_config["AnswerNumber"]["_Locations"]["OperINN"]["x"], rely=second_config["AnswerNumber"]["_Locations"]["OperINN"]["y"])
                        RegionNames.place(relx=second_config["AnswerNumber"]["_Locations"]["RegionName"]["x"], rely=second_config["AnswerNumber"]["_Locations"]["RegionName"]["y"])
                        
if __name__ == "__main__" : _gui().gui()   # Вызов главного класса с его главным модулем