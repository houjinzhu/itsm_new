# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/19 11:19
# software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from itsm.base.base_page import BasePage
from itsm.base.log_until import logger


class RequestListPage(BasePage):
    __MENU_NEW_BUILD = (By.XPATH,"//*[@id='app']/div/div[2]/section/div/div[1]/div[1]/button")
    __BTN_SWITCH_PER = (By.CSS_SELECTOR,".el-icon-tickets")
    __MENU_TITLE = (By.XPATH,'//*[text()="保存成功"]')


    def go_to_newrequest(self):
        logger.info("点击新增按钮")
        self.do_find(self.__MENU_NEW_BUILD).click()

        # self.driver.find_element(By.XPATH,"//*[@id='app']/div/div[2]/section/div/div[1]/div[1]/button").click()

        from itsm.page.new_request_page import NewRequestPage
        return NewRequestPage(self.driver)

    def get_add_msg(self):
        #切换数据显示模式（简约、列表）
        # self.do_find(self.__BTN_SWITCH_PER).click()

        ele = self.wait_element_until_visible(self.__MENU_TITLE)
        logger.info("定位到冒泡数据了")
        msg = ele.text
        logger.info(f"冒泡消息：{msg}")
        return msg