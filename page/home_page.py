# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/18 15:50
# software: PyCharm
from selenium.webdriver.common.by import By

from itsm.base.base_page import BasePage
from itsm.base.log_until import logger
from itsm.page.event_list_page import EventListPage


class HomePage(BasePage):
    __MENU_WORK_ORDER = (By.XPATH,"//*[text()='工单管理']")
    __MENU_REQUEST =(By.XPATH,"//*[text()='请求管理']")
    __MENU_EVENT = (By.XPATH,"//*[text()='事件管理']")


    def go_to_requestlist(self):

        self.do_find(self.__MENU_WORK_ORDER).click()
        self.do_find(self.__MENU_REQUEST).click()
        logger.info("进入列表页面")
        # self.driver.find_element(By.XPATH,"//*[text()='工单管理']").click()
        # self.driver.find_element(By.XPATH,"//*[text()='请求管理']").click()
        from itsm.page.request_list_page import RequestListPage
        return RequestListPage(self.driver)

    def go_to_event(self):
        self.do_find(self.__MENU_WORK_ORDER).click()
        logger.info("点击工单管理成功")
        self.do_find(self.__MENU_EVENT).click()
        logger.info("进入事件列表页面")
        from itsm.page.request_list_page import RequestListPage
        return EventListPage(self.driver)



