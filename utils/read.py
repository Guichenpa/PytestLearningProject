import configparser
import os

import yaml

# 数据的相对路径
# Datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.relpath(__file__))), 'data', 'data.yaml')
Datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data', 'data.yaml')
IniPath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', "settings.ini")


# IniPath = 'E:\Learn\PythonProject\PytestLearningProject\config\settings.ini'
class FileRead:
    def __init__(self):
        self.Datapath = Datapath
        self.IniPath = IniPath

    def read_data(self):
        f = open(self.Datapath, encoding='utf-8')
        data = yaml.safe_load(f)
        return data

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.IniPath, encoding='utf8')
        return config


baseDataRead = FileRead()
