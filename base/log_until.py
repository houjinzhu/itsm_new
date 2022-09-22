# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/18 14:35
# software: PyCharm

import logging

#创建logger实例
logger = logging.getLogger('simple_example')
# 设置日志级别
logger.setLevel(logging.DEBUG)
#流处理器
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#日志打印格式
formatter =logging.Formatter('%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)')
#添加格式配置
ch.setFormatter(formatter)
logger.addHandler(ch)
