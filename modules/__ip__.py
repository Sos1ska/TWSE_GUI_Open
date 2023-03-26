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

class ip:   # Главный класс
    def __init__(self, ip, proxy=bool):   # Модуль который получает аргументы, ну и запускает скрипт по получению данных
        self.ip=ip
        self.__ip__(proxy)
    def __ip__(self, proxy):   # Тело
        @log_start_with_arg("ip.__ip__.__main__", proxy)
        def __main__(proxy):
            if proxy == True : self.__proxy__()
            elif proxy == False : self.__without_proxy__()
    def __without_proxy__(self):   # Орган 1
        _local_ip = self.ip
        @log_start("ip.__without_proxy__.__main__")
        def __main__():
            try : send_request = get(f"http://ip-api.com/json/{_local_ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting")
            except : returns("ip", "503")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Hander = site_json
            structure = {"Continent":Hander["continent"],
                "Country":Hander["country"],
                "regionName":Hander["regionName"],
                "City":Hander["city"],
                "Lat":Hander["lat"],
                "Lon":Hander["lon"],
                "ISP":Hander["isp"],
                "ORG":Hander["org"],
                "AS":Hander["as"],
                "ASName":Hander["asname"],
                "Reverse":Hander["reverse"],
                "Mobile":Hander["mobile"],
                "Proxy":Hander["proxy"],
                "Hosting":Hander["hosting"]
                }
            try:
                with open(os(path+"cache/ip.json"), "w") as file_cache : dump(structure, file_cache)
            except : returns("ip", "424")
            returns("ip", "200")
    def __proxy__(self):   # Орган 2
        _local_ip = self.ip
        @log_start("ip.__proxy__.__main__")
        def __main__():
            with open(os(path+"config/proxy.json"), 'r') as proxy_file : proxy=proxy_file.read()
            try : send_request = get(f"http://ip-api.com/json/{_local_ip}?fields=status,message,continent,country,regionName,city,lat,lon,isp,org,as,asname,reverse,mobile,proxy,hosting", proxies=proxy)
            except : returns("ip", "503")
            answer = send_request
            soup_json = BeautifulSoup(answer.text, "html.parser").text.strip()
            site_json = loads(soup_json)
            Hander = site_json
            structure = {"Continent":Hander["continent"],
                "Country":Hander["country"],
                "regionName":Hander["regionName"],
                "City":Hander["city"],
                "Lat":Hander["lat"],
                "Lon":Hander["lon"],
                "ISP":Hander["isp"],
                "ORG":Hander["org"],
                "AS":Hander["as"],
                "ASName":Hander["asname"],
                "Reverse":Hander["reverse"],
                "Mobile":Hander["mobile"],
                "Proxy":Hander["proxy"],
                "Hosting":Hander["hosting"]
                }
            try:
                with open(os(path+"cache/ip.json"), "w") as file_cache : dump(structure, file_cache)
            except : returns("ip", "424")
            returns("ip", "200")