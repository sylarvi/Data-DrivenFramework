# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11

from Logs.Logger_func import Logger
from configparser import ConfigParser
from PublicConfig.Path_var import config_dir

logger = Logger(logger='config_parser').getlog()


class ConfigInfo:
    def config_parse(self, params):
        config = ConfigParser()
        config.read(config_dir, encoding='utf-8')
        if params == 'localmysql':
            db_info = {'host': config.get(params, 'host'), 'port': config.get(params, 'port'),
                       'user': config.get(params, 'user'), 'password': config.get(params, 'password'),
                       'db_name': config.get(params, 'db_name'), 'charset': config.get(params, 'charset')}
            return db_info
        elif params == 'server':
            server_init = config.get(params, 'server_01')
            return server_init
        else:
            logger.error('can not find infomation in config as {}'.format(params))
            return False


config = ConfigInfo()
if __name__ == '__main__':
    print(ConfigInfo().config_parse('localmysql'))
    print(ConfigInfo().config_parse('server'))
    # print(config_parse('is_run'))
