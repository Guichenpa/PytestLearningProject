import configparser
import os

IniPath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', "settings.ini")


# IniPath = 'E:\Learn\PythonProject\PytestLearningProject\config\settings.ini'


def read_ini():
    config = configparser.ConfigParser()
    config.read(IniPath, encoding='utf8')
    return config


get_ini = read_ini()
