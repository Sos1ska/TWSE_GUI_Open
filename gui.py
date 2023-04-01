from json import load   # Парсинг данных из кэша
from modules.logger import log_start, log_start_with_arg, log_organ   # Лог запуска модулей
from modules.__ip__ import ip as ip_module   # Важные модули
from modules.__mac__ import mac as mac_module
from modules.__number__ import number as number_module
from os import path as folder   # Понимать в какой среде работаем
from os import mkdir   # Создание папки, если нету
from tkinter import *   # Сам движок
from tkinter import ttk
from tkinter import messagebox
from sys import exit

from source.__eng__ import Buttons as Buttons_eng   # Языки
from source.__eng__ import Banners as Banners_eng
from source.__eng__ import Labels as Labels_eng

from source.__rus__ import Buttons as Buttons_rus
from source.__rus__ import Banners as Banners_rus
from source.__rus__ import Labels as Labels_rus

global path
global _cache

def load_py_file(filepath):
    import sys
    _path, fname = folder.split(filepath)
    module, _ = folder.splitext(fname)
        
    if path not in sys.path:            
        sys.path.insert(0, _path)
        
    return __import__(module)

def os(_path):   # Нужен чтобы понимать, что за ОС ну и правильные пути к папкам в ОС
    import os
    if os.sys.platform == "win32" : _path = _path.replace("/", "\\")
    else : _path = _path.replace("\\", "/")
    return _path

path = folder.abspath("work")   # Получить саму рабочаю область

_cache = []
_cache_deleted_ip = []
_cache_deleted_mac = []
_cache_deleted_number = []

if "work" in path : path=path.replace(r"work", "")
else: 
    if "work" in path : path=path.replace(r"work", "")
if folder.exists(os(path+"cache")) == True : pass
else : mkdir(os(path+"cache"))

class config:   # Настройки
    with open(os(path+"config/system.json"), "r") as file_config_load : config = load(file_config_load)
class user_config:
    with open(os(path+"config/user.json"), "r") as file_config_user_load : user_config = load(file_config_user_load)

def _ip():   # Метод получения данных
    # Clear cache number 1
    @log_start("_ip.__main__")
    def __main__():
        try : _local_ip = _gui.IPEntry.get()
        except: 
            messagebox.showwarning(_gui.config["Main"]["_NotificationWarn"]["_Title"], "Entry empty")
            pass
        ip_module(_local_ip, _gui.config["Main"]["Proxy"])
        try:
            with open(os(path+"cache/answer.json.ip"), "r") as file_cache : data_cache_file = load(file_cache)
        except FileNotFoundError as fnfe : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], fnfe)
        match data_cache_file["Answer"]:
            case "200":
                try:
                    match _cache[0]:
                        case "mac":
                            _cache.clear()
                            try:
                                _cache_deleted_mac.append("2")
                                _organ_cache = [_gui_answer.Company, _gui_answer.Address, _gui_answer.Block_Size]
                                for _labels in _organ_cache : _labels.destroy()
                            except : pass
                        case "number":
                            _cache.clear()
                            try:
                                _cache_deleted_number.append("3")
                                _organ_cache = [_gui_answer.OperName, _gui_answer.OperMNC, _gui_answer.OperBrand, _gui_answer.OperINN, _gui_answer.RegionName]
                                for _labels in _organ_cache : _labels.destroy()
                            except : pass
                except IndexError:
                    log_organ("Warn -> \"_ip\" {IndexError}")
                finally:
                    try:
                        match _cache_deleted_ip[0]:
                            case "1":
                                print("Recreate")
                                _gui_answer.Continent = Label(_gui.Main)
                                _gui_answer.Country = Label(_gui.Main)
                                _gui_answer.regionName = Label(_gui.Main)
                                _gui_answer.City = Label(_gui.Main)
                                _gui_answer.LatLon = Label(_gui.Main)
                                _gui_answer.ISP = Label(_gui.Main)
                                _gui_answer.ORG = Label(_gui.Main)
                                _gui_answer.AS = Label(_gui.Main)
                                _gui_answer.ASName = Label(_gui.Main)
                                _gui_answer.Reverse = Label(_gui.Main)
                                _cache_deleted_ip.clear()
                                _gui_answer("ip").Continent.place(relx=_gui.config["AnswerIP"]["_Locations"]["Continent"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["Continent"]["y"])
                                _gui_answer("ip").Country.place(relx=_gui.config["AnswerIP"]["_Locations"]["Country"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["Country"]["y"])
                                _gui_answer("ip").regionName.place(relx=_gui.config["AnswerIP"]["_Locations"]["RegionName"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["RegionName"]["y"])
                                _gui_answer("ip").City.place(relx=_gui.config["AnswerIP"]["_Locations"]["City"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["City"]["y"])
                                _gui_answer("ip").LatLon.place(relx=_gui.config["AnswerIP"]["_Locations"]["LatLon"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["LatLon"]["y"])
                                _gui_answer("ip").ISP.place(relx=_gui.config["AnswerIP"]["_Locations"]["ISP"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["ISP"]["y"])
                                _gui_answer("ip").ORG.place(relx=_gui.config["AnswerIP"]["_Locations"]["ORG"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["ORG"]["y"])
                                _gui_answer("ip").AS.place(relx=_gui.config["AnswerIP"]["_Locations"]["AS"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["AS"]["y"])
                                _gui_answer("ip").ASName.place(relx=_gui.config["AnswerIP"]["_Locations"]["ASName"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["ASName"]["y"])
                                _gui_answer("ip").Reverse.place(relx=_gui.config["AnswerIP"]["_Locations"]["Reverse"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["Reverse"]["y"])
                    except IndexError:
                        print("Index IP")
                        _gui_answer("ip").Continent.place(relx=_gui.config["AnswerIP"]["_Locations"]["Continent"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["Continent"]["y"])
                        _gui_answer("ip").Country.place(relx=_gui.config["AnswerIP"]["_Locations"]["Country"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["Country"]["y"])
                        _gui_answer("ip").regionName.place(relx=_gui.config["AnswerIP"]["_Locations"]["RegionName"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["RegionName"]["y"])
                        _gui_answer("ip").City.place(relx=_gui.config["AnswerIP"]["_Locations"]["City"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["City"]["y"])
                        _gui_answer("ip").LatLon.place(relx=_gui.config["AnswerIP"]["_Locations"]["LatLon"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["LatLon"]["y"])
                        _gui_answer("ip").ISP.place(relx=_gui.config["AnswerIP"]["_Locations"]["ISP"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["ISP"]["y"])
                        _gui_answer("ip").ORG.place(relx=_gui.config["AnswerIP"]["_Locations"]["ORG"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["ORG"]["y"])
                        _gui_answer("ip").AS.place(relx=_gui.config["AnswerIP"]["_Locations"]["AS"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["AS"]["y"])
                        _gui_answer("ip").ASName.place(relx=_gui.config["AnswerIP"]["_Locations"]["ASName"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["ASName"]["y"])
                        _gui_answer("ip").Reverse.place(relx=_gui.config["AnswerIP"]["_Locations"]["Reverse"]["x"], rely=_gui.config["AnswerIP"]["_Locations"]["Reverse"]["y"])
            case "424" : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], "Code error 424")
            case "503" : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], "Code error 503")

def _mac():   # Clear cache number 2
    @log_start("_mac.__main__")
    def __main__():
        try : _local_mac = _gui.MACEntry.get()
        except: 
            messagebox.showwarning(_gui.config["Main"]["_NotificationWarn"]["_Title"], "Entry empty")
            pass
        mac_module(_local_mac, _gui.config["Main"]["Proxy"])
        try:
            with open(os(path+"cache/answer.json.mac"), "r") as file_cache : data_cache_file = load(file_cache)
        except FileNotFoundError as fnfe : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], fnfe)
        match data_cache_file["Answer"]:
            case "200":
                try:
                    match _cache[0]:
                        case "ip":
                            _cache.clear()
                            try:
                                _cache_deleted_ip.append("1")
                                _organ_cache = [_gui_answer.Continent, _gui_answer.Country, _gui_answer.regionName, _gui_answer.City, _gui_answer.LatLon, _gui_answer.ISP, _gui_answer.ORG, _gui_answer.AS, _gui_answer.ASName, _gui_answer.Reverse]
                                for _labels in _organ_cache : _labels.destroy()
                            except : pass
                    match _cache[0]:
                        case "number":
                            _cache.clear()
                            try:
                                _cache_deleted_number.append("3")
                                _organ_cache = [_gui_answer.OperName, _gui_answer.OperMNC, _gui_answer.OperBrand, _gui_answer.OperINN, _gui_answer.RegionName]
                                for _labels in _organ_cache : _labels.destroy()
                            except : pass
                except IndexError : log_organ("Warn -> \"_mac\" {IndexError}")
                finally:
                    try:
                        match _cache_deleted_mac[0]: 
                            case "2":
                                print("Recreate")
                                _gui_answer.Company = Label(_gui.Main)
                                _gui_answer.Address = Label(_gui.Main)
                                _gui_answer.Block_Size = Label(_gui.Main)
                                _cache_deleted_mac.clear()
                                _gui_answer.Company.config()
                                _gui_answer("mac").Company.place(relx=_gui.config["AnswerMAC"]["_Locations"]["Company"]["x"], rely=_gui.config["AnswerMAC"]["_Locations"]["Company"]["y"])
                                _gui_answer("mac").Address.place(relx=_gui.config["AnswerMAC"]["_Locations"]["Address"]["x"], rely=_gui.config["AnswerMAC"]["_Locations"]["Address"]["y"])
                                _gui_answer("mac").Block_Size.place(relx=_gui.config["AnswerMAC"]["_Locations"]["Block_Size"]["x"], rely=_gui.config["AnswerMAC"]["_Locations"]["Block_Size"]["y"])
                    except IndexError:
                        print("Index MAC")
                        _gui_answer("mac").Company.place(relx=_gui.config["AnswerMAC"]["_Locations"]["Company"]["x"], rely=_gui.config["AnswerMAC"]["_Locations"]["Company"]["y"])
                        _gui_answer("mac").Address.place(relx=_gui.config["AnswerMAC"]["_Locations"]["Address"]["x"], rely=_gui.config["AnswerMAC"]["_Locations"]["Address"]["y"])
                        _gui_answer("mac").Block_Size.place(relx=_gui.config["AnswerMAC"]["_Locations"]["Block_Size"]["x"], rely=_gui.config["AnswerMAC"]["_Locations"]["Block_Size"]["y"])
            case "424" : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], "Code error 424")
            case "503" : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], "Code error 503")

def _number():   # Clear cache number 3
    @log_start("_number.__main__")
    def __main__():
        try : _local_number = _gui.NumberEntry.get()
        except: 
            messagebox.showwarning(_gui.config["Main"]["_NotificationWarn"]["_Title"], "Entry empty")
            pass
        number_module(_local_number, _gui.config["Main"]["Proxy"])
        try:
            with open(os(path+"cache/answer.json.number"), "r") as file_cache : data_cache_file = load(file_cache)
        except FileNotFoundError as fnfe : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], fnfe)
        match data_cache_file["Answer"]:
            case "200":
                try:
                    match _cache[0]:
                        case "ip":
                            _cache.clear()
                            try:
                                _cache_deleted_ip.append("1")
                                _organ_cache = [_gui_answer.Continent, _gui_answer.Country, _gui_answer.regionName, _gui_answer.City, _gui_answer.LatLon, _gui_answer.ISP, _gui_answer.ORG, _gui_answer.AS, _gui_answer.ASName, _gui_answer.Reverse]
                                for _labels in _organ_cache : _labels.destroy()
                            except : pass
                    match _cache[0]:
                        case "mac":
                            _cache.clear()
                            try:
                                _cache_deleted_mac.append("2")
                                _organ_cache = [_gui_answer.Company, _gui_answer.Address, _gui_answer.Block_Size]
                                for _labels in _organ_cache : _labels.destroy()
                            except : pass
                except IndexError : log_organ("Warn -> \"_number\" {IndexError}")
                finally:
                    try:
                        match _cache_deleted_number[0]:
                            case "3":
                                print("Recreate")
                                _gui_answer.OperName = Label(_gui.Main)
                                _gui_answer.OperMNC = Label(_gui.Main)
                                _gui_answer.OperBrand = Label(_gui.Main)
                                _gui_answer.OperINN = Label(_gui.Main)
                                _gui_answer.RegionName = Label(_gui.Main)
                                _cache_deleted_number.clear()
                                _gui_answer("number").OperName.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperName"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperName"]["y"])
                                _gui_answer("number").OperMNC.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperMNC"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperMNC"]["y"])
                                _gui_answer("number").OperBrand.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperBrand"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperBrand"]["y"])
                                _gui_answer("number").OperINN.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperINN"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperINN"]["y"])
                                _gui_answer("number").RegionName.place(relx=_gui.config["AnswerNumber"]["_Locations"]["RegionName"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["RegionName"]["y"])
                    except IndexError:
                        print("Index Number")
                        _gui_answer("number").OperName.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperName"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperName"]["y"])
                        _gui_answer("number").OperMNC.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperMNC"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperMNC"]["y"])
                        _gui_answer("number").OperBrand.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperBrand"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperBrand"]["y"])
                        _gui_answer("number").OperINN.place(relx=_gui.config["AnswerNumber"]["_Locations"]["OperINN"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["OperINN"]["y"])
                        _gui_answer("number").RegionName.place(relx=_gui.config["AnswerNumber"]["_Locations"]["RegionName"]["x"], rely=_gui.config["AnswerNumber"]["_Locations"]["RegionName"]["y"])
            case "424" : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], "Code error 424")
            case "503" : messagebox.showerror(_gui.config["Main"]["_Notification"]["_Title"], "Code error 503")

def _quit():    # Модуль для выхода из ПО
    exit(1)

class _gui:    # Главный класс, который создаёт окно для пользователя

    Main = Tk()    # Корень главного окна

    config = config.config    # Получение настроек из класса config
    user_config = user_config.user_config
    
    IPEntry = Entry(Main)   # Поле для IP-Адреса

    MACEntry = Entry(Main)   # Поле для MAC-Адреса

    NumberEntry = Entry(Main)   # Поле для номера телефона

    match user_config["Language"]:
        case "english":
            IPButton = ttk.Button(Main, text=Buttons_eng.out[0], command=_ip)   # Ну тут логично. Кнопки
            MACButton = ttk.Button(Main, text=Buttons_eng.out[1], command=_mac)
            NumberButton = ttk.Button(Main, text=Buttons_eng.out[2], command=_number)
            Quit = ttk.Button(Main, text=Buttons_eng.out[3], command=_quit)
        case "russia":
            IPButton = ttk.Button(Main, text=Buttons_rus.out[0], command=_ip)   # Ну тут логично. Кнопки
            MACButton = ttk.Button(Main, text=Buttons_rus.out[1], command=_mac)
            NumberButton = ttk.Button(Main, text=Buttons_rus.out[2], command=_number)
            Quit = ttk.Button(Main, text=Buttons_rus.out[3], command=_quit)

    def gui(self):   # Создание окна
        @log_start("_gui.gui.__main__")
        def __main__():
            self.Main.title(self.config["Main"]["_Title"])
            geometry_x = self.config["Main"]["_Screen"]["x"]
            geometry_y = self.config["Main"]["_Screen"]["y"]
            self.Main.geometry(f"{geometry_x}x{geometry_y}")
            self.Main.resizable(False, False)
            self.Main.iconbitmap(os(path+self.config["Main"]["_Ico"]))
            _micro_window().__main__()
            self._buttons()
            self._entrys()
            self._labels()
            self._banners()
        self.Main.mainloop()

    def _labels(self):   # Создание текста
        @log_start("_gui._label.__main__")
        def __main_old__():
            match self.user_config["Language"]:
                case "english":
                    IP = Label(self.Main, text=Labels_eng.out[0], font=("", 15))
                    MAC = Label(self.Main, text=Labels_eng.out[1], font=("", 15))
                    Number = Label(self.Main, text=Labels_eng.out[2], font=("", 15))
                case "russia":
                    IP = Label(self.Main, text=Labels_rus.out[0], font=("", 15))
                    MAC = Label(self.Main, text=Labels_rus.out[1], font=("", 15))
                    Number = Label(self.Main, text=Labels_rus.out[2], font=("", 15))
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

    def _banners(self):   # Создание баннеров
        @log_start("_gui._banners.__main__")
        def __main__():
            match self.user_config["Language"]:
                case "english":
                    Banner1 = Label(self.Main, text=Banners_eng.out[0], font=("", 15))
                case "russia":
                    Banner1 = Label(self.Main, text=Banners_rus.out[0], font=("", 15))
            Banner1.place(relx=self.config["Main"]["_Locations"]["_Banner1"]["x"], rely=self.config["Main"]["_Locations"]["_Banner1"]["y"])

class _micro_window(_gui):
    Main = _gui.Main
    c = Canvas(Main, width=300, height=450)
    def __main__(self):
        try : self.c.place(relx=self.config["Main"]["_Locations"]["_Micro_Window"]["x"], rely=self.config["Main"]["_Locations"]["_Micro_Window"]["y"])
        except Exception as ex : print(ex), quit()
        finally : self.c.create_rectangle(15, 15, 300, 420)

class _gui_answer(_gui):   # "Подручный класс". Я считаю его подручным, т.к. он создаёт нам уже окно ответа
    Continent = Label(_gui.Main)
    Country = Label(_gui.Main)
    regionName = Label(_gui.Main)
    City = Label(_gui.Main)
    LatLon = Label(_gui.Main)
    ISP = Label(_gui.Main)
    ORG = Label(_gui.Main)
    AS = Label(_gui.Main)
    ASName = Label(_gui.Main)
    Reverse = Label(_gui.Main)

    Company = Label(_gui.Main)
    Address = Label(_gui.Main)
    Block_Size = Label(_gui.Main)

    OperName = Label(_gui.Main)
    OperMNC = Label(_gui.Main)
    OperBrand = Label(_gui.Main)
    OperINN = Label(_gui.Main)
    RegionName = Label(_gui.Main)
    def __init__(self, _mode):
        match _mode:
            case "ip":
                _cache.append("ip")
                with open(os(path+"cache/ip.json"), "r") as json_cache : upload = load(json_cache)
                self.Continent.config(text=upload["Continent"])
                self.Country.config(text=upload["Country"])
                self.regionName.config(text=upload["regionName"])
                self.City.config(text=upload["City"])
                self.LatLon.config(text=str(upload["Lat"])+" "+str(upload["Lon"]))
                self.ISP.config(text=upload["ISP"])
                self.ORG.config(text=upload["ORG"])
                self.AS.config(text=upload["AS"])
                self.ASName.config(text=upload["ASName"])
                self.Reverse.config(text=upload["Reverse"])
            case "mac":
                _cache.append("mac")
                with open(os(path+"cache/mac.json"), "r") as json_cache : upload = load(json_cache)
                self.Company.config(text=upload["Company"])
                self.Address.config(text=upload["Address"])
                self.Block_Size.config(text=upload["Block_Size"])
            case "number":
                _cache.append("number")
                with open(os(path+"cache/number.json"), "r") as json_cache : upload = load(json_cache)
                self.OperName.config(text=upload["OperName"])
                self.OperMNC.config(text=upload["OperMNC"])
                self.OperBrand.config(text=upload["OperBrand"])
                self.OperINN.config(text=upload["OperINN"])
                self.RegionName.config(text=upload["RegionName"])
            case _ : pass
if __name__ == "__main__" : _gui().gui()
