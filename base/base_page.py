# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/13 16:09
# software: PyCharm


import time

import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _BASE_URL =""
    def __init__(self, base_driver=None):
        if base_driver:
            self.driver = base_driver
        else:
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()

        #如果不是http开头的就导航到新的地址当中
        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)


    def do_find(self,by,locator=None):
        #获取单个元素
        if locator:
            return self.driver.find_element(by, locator)
        else:
            return self.driver.find_element(*by)

    def do_finds(self,by,locator=None):
        #获取多个元素
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    def do_send_keys(self,value,by,locator=None):
        ele = self.do_find(by,locator)
        # ele.clear()
        ele.send_keys(value)

    def do_send_keys_clear(self,value,by,locator=None):
        ele = self.do_find(by,locator)
        ele.clear()
        ele.send_keys(value)


    def do_quit(self):
        self.driver.quit()

    #截图
    def get_search(self):

        timestamp = int(time.time())
        image_path = f'./images/image_{timestamp}.PNG'
        #截图
        self.driver.save_screenshot(image_path)
        #将截图放到报告数据中
        allure.attach.file(image_path,name="picture",attachment_type=allure.attachment_type.PNG)


        # 进行测试：进入当前文件夹内，执行：pytest 文件名称 --alluredir=./resurt
        # 查看测试报告：allure serve ./resurt


    def wait_element_until_visible(self,locator:tuple):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
