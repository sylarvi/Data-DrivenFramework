# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11
import requests
from PublicConfig.Useragent_config import useragent
from Utils.Cookie_handle import get_cookie_value, write_cookie


class BaseRequest:

    def send_post(self, url, data, cookie_id):
        if cookie_id == 0:
            res = requests.post(url=url, data=data, cookies=None, headers=useragent, verify=False)
        elif cookie_id == 1:
            cookie = get_cookie_value('cookie')
            res = requests.post(url=url, data=data, cookies=cookie, headers=useragent, verify=False)
        elif cookie_id == 2:
            res = requests.post(url=url, data=data, cookies=None, headers=useragent, verify=False)
            cookie = requests.utils.dict_from_cookiejar(res.cookies)
            write_cookie(cookie, 'cookies')

        return res

    def send_get(self, url, data, cookie_id):
        if cookie_id == 0:
            res = requests.get(url=url, params=data, cookies=None, headers=useragent, verify=False)
        elif cookie_id == 1:
            cookie = get_cookie_value('cookie')
            res = requests.get(url=url, params=data, cookies=cookie, headers=useragent, verify=False)
        elif cookie_id == 2:
            res = requests.get(url=url, params=data, cookies=None, headers=useragent, verify=False)
            cookie = requests.utils.dict_from_cookiejar(res.cookies)
            write_cookie(cookie, 'cookies')

        return res

    def send_put(self, url, data, cookie_id):
        if cookie_id == 0:
            res = requests.put(url=url, params=data, cookies=None, headers=useragent, verify=False)
        elif cookie_id == 1:
            cookie = get_cookie_value('cookie')
            res = requests.put(url=url, params=data, cookies=cookie, headers=useragent, verify=False)
        elif cookie_id == 2:
            res = requests.put(url=url, params=data, cookies=None, headers=useragent, verify=False)
            cookie = requests.utils.dict_from_cookiejar(res.cookies)
            write_cookie(cookie, 'cookies')

        return res

    def run(self, method, url, data, cookie_id):
        if method == 'GET':
            res = self.send_get(url, data, cookie_id)
        elif method == 'POST':
            res = self.send_post(url, data, cookie_id)
        else:
            res = self.send_put(url, data, cookie_id)
        return res


request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
    response = request.run('GET','http://api.nnzhp.cn/api/user/stu_info', {'stu_name': 'b'}, 0)
    res = request.run('GET','http://api.nnzhp.cn/api/user/stu_info', {'stu_name': 'b'}, 0).json()
    print(res)
    print(response.status_code)

# a = {'error_code': 0, 'stu_info': [{'id': 1043, 'name': 'B', 'sex': '?', 'age': 18, 'addr': '????', 'grade': '??', 'phone': '13197390530', 'gold': 100}]}
