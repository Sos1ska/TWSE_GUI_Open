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

class mac:   # Главный класс
    def __init__(self, mac, proxy=bool):   # Модуль который получает аргументы, ну и запускает скрипт по получению данных
        self.mac=mac
        self.__mac__(proxy)
    def __mac__(self, proxy):   # Тело
        @log_start_with_arg("mac.__mac__.__main__", proxy)
        def __main__(proxy):
            if proxy == True : self.__proxy__()
            elif proxy == False : self.__without_proxy__()
    def __without_proxy__(self):   # Орган 1
        _local_mac = self.mac
        @log_start("mac.__without_proxy__.__main__")
        def __main__():
            try : send_request = get(f"https://api.2ip.ua/mac.json?mac={_local_mac}")
            except : returns("mac", "503")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            structure = {"Company":Handler["company"],
            "Address":Handler["address"],
            "Block_Size":Handler["block_size"]}
            try:
                with open(os(path+"cache/mac.json"), "w") as file_cache : dump(structure, file_cache)
            except : returns("mac", "424")
            returns("mac", "200")
    def __proxy__(self):   # Орган 2
        _local_mac = self.mac
        @log_start("mac.__proxy__.__main__")          
        def __main__():
            with open(os(path+"config/proxy.json"), 'r') as proxy_file : proxy=proxy_file.read()
            try : send_request = get(f"https://api.2ip.ua/mac.json?mac={_local_mac}", proxies=proxy)
            except : returns("mac", "503")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Handler = site_json
            structure = {"Company":Handler["company"],
            "Address":Handler["address"],
            "Block_Size":Handler["block_size"]}
            try:
                with open(os(path+"cache/mac.json"), "w") as file_cache : dump(structure, file_cache)
            except : returns("mac", "424")
            returns("mac", "200")