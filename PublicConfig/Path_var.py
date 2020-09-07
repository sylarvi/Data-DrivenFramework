# -*-coding:utf-8 -*-
# @Author: lixiao
# Created on: 2020-08-11
import os

# 项目路径
project_dir = os.path.dirname(os.path.dirname(__file__))

# 数据库配置文件路径
config_dir = os.path.join(project_dir, "PublicConfig", "Public_config.ini").replace("\\", "/")

if __name__ == "__main__":
    print(project_dir)
    print(config_dir)
