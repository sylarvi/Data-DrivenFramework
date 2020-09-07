# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11

import ddt
import json
import unittest
from Logs.Logger_func import Logger
from Base.Base_request import request
from Utils.Json_diff import json_diff
from Utils.Excel_handle import HandleExcel
from Utils.Data_structure import get_case_data

logger = Logger(logger='test_case01').getlog()
data = get_case_data()


@ddt.ddt
class TestCase01(unittest.TestCase):
    @ddt.data(*data)
    def test_case(self, data):
        logger.info('开始执行测试用例:{}'.format(data[0]))
        logger.info('测试功能点为:{}'.format(data[1]))
        logger.info('测试用例前置条件为:{}'.format(data[2]))
        logger.info('测试用例依赖key为:{}'.format(data[3]))
        logger.info('测试url为:{}'.format(data[4]))
        logger.info('请求方法为:{}'.format(data[5]))
        logger.info('测试结果判断方法为:{}'.format(data[8]))
        logger.info('测试预期结果为:{}'.format(data[9]))
        response = request.run(data[5], data[4], json.loads(data[6]), int(data[7]))
        logger.info('返回结果为:{}'.format(response.json()))
        logger.info('返回状态码为:{}'.format(response.status_code))
        HandleExcel().write_data(HandleExcel().get_case_number(data[0]), 13, str(response.json()))

        try:
            self.assertEqual(200, response.status_code)
            self.assertTrue(json_diff(data[0], response.json()))
            HandleExcel().write_data(HandleExcel().get_case_number(data[0]), 12, 'Pass')
        except AssertionError as e:
            logger.error(e)
            HandleExcel().write_data(HandleExcel().get_case_number(data[0]), 12, 'Failed')
        self.assertEqual(200, response.status_code)
        self.assertTrue(json_diff(data[0], response.json()))


if __name__ == '__main__':
    unittest.main()
