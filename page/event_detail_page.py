# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/21 14:07
# software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from itsm.base.base_page import BasePage
from itsm.base.log_until import logger

class EventDetailPsge(BasePage):

    __BTN_ASSIGN = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[5]/div[2]/div/div/div[1]/button[2]/span')
    __INPUT_GROUP = (By.XPATH,'//*[text()="处理组:"]/../div')
    __MENU_GROUP = (By.XPATH,'//*[text()="侯金竹处理组"]')
    __INPUT_PERSON = (By.XPATH,'//*[text()="处理人:"]/../div')
    __MENU_PERSON = (By.XPATH, '//*[text()="侯金竹"]')
    ___BTN_PRESERVATION = (By.XPATH,'//*[text()="处理组:"]/../../../div/button[2]')

    def assign_event(self):
        logger.info("进入详情页面")
        self.do_find(self.__BTN_ASSIGN).click()
        sleep(2)
        self.do_find(self.__INPUT_GROUP).click()
        # self.do_send_keys("侯金竹处理组",self.__INPUT_GROUP)
        logger.info("处理组获取成功")
        # 滚动查找
        # js = "window.scrollTo(0,document.body.scrollHeight)"
        # self.driver.execute_script(js)
        # sleep(5)
        self.wait_element_until_visible(self.__INPUT_GROUP)
        self.do_find(self.__MENU_GROUP).click()
        logger.info("添加处理组成功")
        self.do_find(self.__INPUT_PERSON).click()
        self.do_find(self.__MENU_PERSON).click()
        logger.info("选择处理人成功")
        self.do_find(self.___BTN_PRESERVATION).click()






