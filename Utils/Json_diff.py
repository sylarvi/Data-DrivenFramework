# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11

from deepdiff import DeepDiff
from Utils.Json_handle import get_value


def json_diff(kw, request_data):
    """判断两个字典数据类型是否一致"""
    src_data = get_value(kw, file_name='result.json')
    # print(src_data)
    if isinstance(src_data, dict) and isinstance(request_data, dict):
        diff_result = DeepDiff(src_data, request_data, ignore_order=True).to_dict()
        if diff_result.get("dictionary_item_added") or diff_result.get('iterable_item_removed') or diff_result.get("dictionary_item_removed") or diff_result.get('iterable_item_added'):
            return False
        else:
            return True
    else:
        return 'Data type error'


if __name__ == '__main__':
    dict01 = {"error_code": 0,
              "stu_info": [
                  {
                      "id": 1143,
                      "sex1": ''},
                  {
                      "id": 1543,
                      "sex1": ''}
              ]
              }
    c = get_value('dict01', file_name='result.json')
    result = json_diff('dict01', dict01)
    print(result)
    diff_result = DeepDiff(c, dict01, ignore_order=True).to_dict()
    print(diff_result)