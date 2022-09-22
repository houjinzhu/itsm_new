# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/13 16:06
# software: PyCharm
import logging
import random
from time import sleep

# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from itsm.base.base_page import BasePage
from itsm.base.log_until import logger





class LoginPage(BasePage):
    _BASE_URL = "http://xxx.xx.xx/login"
    __INPUT_USERNAME = (By.CSS_SELECTOR,"[placeholder='账号']")
    __INPUT_PASSWORD = (By.CSS_SELECTOR,"[placeholder='密码']")
    __BTN_LOGIN = (By.XPATH,"//*[@class='el-button el-button--primary el-button--medium']")

    def login(self):
        logger.info("登录")
        self.do_send_keys("admin",self.__INPUT_USERNAME)
        self.do_send_keys("admin",self.__INPUT_PASSWORD)
        self.do_find(self.__BTN_LOGIN).click()


        #避免链式调用出错
        from itsm.page.home_page import HomePage
        #使用self.driver是需要上一个driver，否则会一个步骤就打开一个driver
        return HomePage(self.driver)


    # def reuse_browser(self):
    #     logger.info("复用浏览器")
    #     option = Options()
    #
    #     # 修改实例属性为debug模式启动的ip+端口
    #     option.debugger_address = "localhost:9222"
    #
    #     self._driver = webdriver.Chrome(options=option)
    #
    #     self._driver.get(self._BASE_URL)
    #     sleep(15)






