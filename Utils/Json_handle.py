# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11

import json
from PublicConfig.Path_var import project_dir


def read_json(file_name=None):
    """读取json配置文件的数据"""
    if file_name == None:
        file_path = project_dir + "/PublicConfig/cookie.json"
    else:
        file_path = project_dir + "/PublicConfig/" + file_name
    with open(file_path, encoding='UTF-8') as f:
        data = json.load(f)
    return data


def get_value(key, file_name=None):
    """根据给定的key获取json配置文件中的值"""
    data = read_json(file_name)
    return data.get(key)


def write_value(data, file_name=None):
    """写入json文件数据"""
    data_value = json.dumps(data)
    if file_name == None:
        path = project_dir + "/PublicConfig/cookie.json"
    else:
        path = project_dir + file_name
    with open(path, "w") as f:
        f.write(data_value)


if __name__ == "__main__":
    print(get_value('app'))
    print(get_value('api_006', file_name='result.json'))