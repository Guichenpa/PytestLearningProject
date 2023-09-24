import os

import yaml

# 数据的相对路径
Datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', 'data.yaml')


def read_data():
    f = open(Datapath, encoding='utf-8')
    data = yaml.safe_load(f)
    return data


get_data = read_data()
