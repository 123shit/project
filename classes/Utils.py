import os
import time
import configparser as ConfigParser

class Util:

    def __init__(self):
        return

    def getTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 系统配置类
class Config:

    _config = ConfigParser.ConfigParser()

    def __init__(self):
        _basedir = os.path.dirname(__file__)
        print(_basedir + "/../config/config.ini")
        Config._config.read(_basedir + "/../config/config.ini")
        return

    def get(self, section, key):
        return Config._config.get(section, key)

    def getInt(self, section, key):
        return Config._config.getint(section, key)