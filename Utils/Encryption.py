# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11

import hashlib


def encrypt(content):
    md5 = hashlib.md5()
    md5.update(content.encode('utf-8'))
    result = md5.hexdigest()
    return result


if __name__ == '__main__':
    print(encrypt('传输内容'))
    # 6d0155234ae30ed6064a7f40bcf4f336