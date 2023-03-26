# Файл для логинга, тут ничего интересного нету
import datetime
from os import path as folder
from json import load, dump
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

config_path = path+'config/system.json'

with open(f"{os(_path=config_path)}", "r") as config: 
    data = load(config)
    user = data["Log"]["LogName"]

def log_start_with_arg(name, args):
    def _log(func):
        try: 
            f = open(f'{os(_path=path)}log.txt', 'a')
            local_mode = 'a'
        except FileNotFoundError: 
            f = open(f'{os(_path=path)}log.txt', 'w')
            local_mode = 'a'
        f.write(f"[ {user} ] - [ Start work -> {name} ] --- {str(datetime.datetime.now())}\n")
        f.close()
        try : func(args)
        except:
            f = open(f'{os(_path=path)}log.txt', local_mode)
            f.write(f"[ {user} ] - [ End work with error -> {name} ] --- {str(datetime.datetime.now())}\n")
            f.close()
            quit()
        f = open(f'{os(_path=path)}log.txt', local_mode)
        f.write(f"[ {user} ] - [ End work -> {name} ] --- {str(datetime.datetime.now())}\n")
        f.close()
        return func
    return _log

def log_start(name):
    def _log(func):
        try: 
            f = open(f'{os(_path=path)}log.txt', 'a')
            local_mode = 'a'
        except FileNotFoundError: 
            f = open(f'{os(_path=path)}log.txt', 'w')
            local_mode = 'a'
        f.write(f"[ {user} ] - [ Start work -> {name} ] --- {str(datetime.datetime.now())}\n")
        f.close()
        try : func()
        except:
            f = open(f'{os(_path=path)}log.txt', local_mode)
            f.write(f"[ {user} ] - [ End work with error -> {name} ] --- {str(datetime.datetime.now())}\n")
            f.close()
            quit()
        f = open(f'{os(_path=path)}log.txt', local_mode)
        f.write(f"[ {user} ] - [ End work -> {name} ] --- {str(datetime.datetime.now())}\n")
        f.close()
        return func
    return _log

def returns(name, code):
    with open(os(path+f"cache/answer.json.{name}"), "w") as file_return: 
        if code == "503" or code == "424" : dump({"Answer":code}, file_return), quit()
        elif code == "200" : dump({"Answer":code}, file_return)