# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11

from Utils.Json_handle import read_json, write_value


def get_cookie_value(key):
    """获取保存在json文件的cookie"""
    data = read_json()
    return data[key]


def write_cookie(cookie, key):
    """在发送请求后获得cookie值写入json文件"""
    data = read_json()
    data[key] = cookie
    write_value(data)


if __name__ == '__main__':
    print(get_cookie_value('cookies'))
    a = {"cookie": 'KcqDuYMYptXfoTyu4fCaCcU0lysbok6UZ_-R0rwnIuvaazxu888'}
    write_cookie(a, 'cookies')