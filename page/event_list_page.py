# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/21 13:56
# software: PyCharm
from selenium.webdriver.common.by import By

from itsm.base.base_page import BasePage

from itsm.base.log_until import logger
from itsm.page.event_detail_page import EventDetailPsge


class EventListPage(BasePage):

    __MENU_EVENT_ID = (By.XPATH,'//*[@id="app"]/div/div[2]/section/div/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/button')
    __BTN_SWITCH_PER = (By.CSS_SELECTOR, ".el-icon-tickets")

    def go_to_event_detail(self):
        logger.info("切换视图")
        self.wait_element_until_visible(self.__BTN_SWITCH_PER)
        self.do_find(self.__BTN_SWITCH_PER).click()
        self.do_find(self.__MENU_EVENT_ID).click()
        ele = self.do_find(self.__MENU_EVENT_ID)
        msg = ele.text
        logger.info(f"订单ID：{msg}")


        return EventDetailPsge(self.driver)

