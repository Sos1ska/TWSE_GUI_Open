from requests import get   # Отправка запроса
from bs4 import BeautifulSoup   # Парсинг данных на html-json уровне, ну и расшифровать. Ведь данные приходят в виде byte
from json import loads, dump   # Высасывание данных из json
from os import path as folder   # Понимать в какой среде работаем
from .logger import log_start_with_arg, log_start, returns   # Лог и не только
global path

def os(_path):
    import os
    if os.sys.platform == "win32" : _path = _path.replace("/", "\\")
    else : _path = _path.replace("\\", "/")
    return _path

path = folder.abspath("work")

if "work" in path : path=path.replace(r"work", "")
else: 
    if "work" in path : path=path.replace(r"work", "")

class number:   # Главный класс
    def __init__(self, number, proxy=bool):   # Модуль который получает аргументы, ну и запускает скрипт по получению данных
        self.number=number
        self.__number__(proxy)
    def __number__(self, proxy):   # Тело
        @log_start_with_arg("number.__number__.__main__", proxy)
        def __main__(proxy):
            if proxy == True : self.__proxy__()
            elif proxy == False : self.__without_proxy__()
    def __without_proxy__(self):   # Орган 1
        _local_number = self.number
        @log_start("number.__without_proxy__.__main__")
        def __main__():
            try : send_request = get(f"https://htmlweb.ru/json/mnp/phone/{_local_number}")
            except : returns("number", "503")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            structure = {"OperName":Handler["oper"]["name"],
            "OperMNC":Handler["oper"]["mnc"],
            "OperBrand":Handler["oper"]["brand"],
            "OperINN":Handler["oper"]["inn"],
            "WorkedMobile":Handler["mobile"],
            "RegionName":Handler["region"]["name"]}
            try:
                with open(os(path+"cache/number.json"), "w") as file_cache : dump(structure, file_cache)
            except : returns("number", "424")
            returns("number", "200")
    def __proxy__(self):   # Орган 2
        _local_number = self.number
        @log_start("number.__proxy__.__main__")
        def __main__():
            with open(os(path+"config/proxy.json"), 'r') as proxy_file : proxy=proxy_file.read()
            try : send_request = get(f"https://htmlweb.ru/json/mnp/phone/{_local_number}", proxies=proxy)
            except : returns("number", "503")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            structure = {"OperName":Handler["oper"]["name"],
            "OperMNC":Handler["oper"]["mnc"],
            "OperBrand":Handler["oper"]["brand"],
            "OperINN":Handler["oper"]["inn"],
            "WorkedMobile":Handler["mobile"],
            "RegionName":Handler["region"]["name"]}
            try:
                with open(os(path+"cache/number.json"), "w") as file_cache : dump(structure, file_cache)
            except : returns("number", "424")
            returns("number", "200")