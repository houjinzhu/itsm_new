# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/18 15:59
# software: PyCharm
import random
from time import sleep

from selenium.webdriver.common.by import By

from itsm.base.base_page import BasePage
from itsm.base.log_until import logger


class NewRequestPage(BasePage):

    __INPUT_FIR_CLA = (By.CSS_SELECTOR,"[placeholder='请选择一级分类']")
    __MENU_FIR_CLA1 = (By.XPATH,"//*[text()='xxx']")
    __INPUT_SEC_CLA = (By.CSS_SELECTOR,"[placeholder='请选择二级分类']")
    __MENU_SEC_CLA1 = (By.XPATH,"//*[text()='xxx']")
    __INPUT_THI_CLA = (By.CSS_SELECTOR,"[placeholder='请选择三级分类']")
    __MENU_THI_CLA1 = (By.XPATH,"//*[text()='xxx']")
    __INPUT_NAME = (By.XPATH,"//*[@maxlength='200']")
    __INPUT_DESCRIBE = (By.CSS_SELECTOR,".el-textarea__inner")
    __BTN_PRESERVATION = (By.XPATH,"//*[text()='保存']")


    def new_request(self,order_name):
        logger.info("新增数据")
        self.do_send_keys("应用系统",self.__INPUT_FIR_CLA)
        self.do_find(self.__MENU_FIR_CLA1).click()
        logger.info("一级分类")
        self.do_send_keys("BPC",self.__INPUT_SEC_CLA)
        self.do_find(self.__MENU_SEC_CLA1).click()
        self.do_send_keys("BPC登录问题",self.__INPUT_THI_CLA)
        self.do_find(self.__MENU_THI_CLA1).click()
        logger.info("选择分类成功")

        self.do_send_keys(f"selenium test{order_name}",self.__INPUT_NAME)
        logger.info(f"新增订单名称是:selenium test{order_name}")

        self.do_send_keys("test,test",self.__INPUT_DESCRIBE)
        self.do_find(self.__BTN_PRESERVATION).click()
        from itsm.page.request_list_page import RequestListPage
        return RequestListPage(self.driver)


    # def new_request(self,order_name):
    #     logger.info("新增数据")
    #     self.driver.find_element(By.CSS_SELECTOR, "[placeholder='请选择一级分类']").send_keys("应用系统")
    #     self.driver.find_element(By.XPATH, "//*[text()='应用系统']").click()
    #     self.driver.find_element(By.CSS_SELECTOR, "[placeholder='请选择二级分类']").send_keys("BPC")
    #     self.driver.find_element(By.XPATH, "//*[text()='BPC']").click()
    #     self.driver.find_element(By.CSS_SELECTOR, "[placeholder='请选择三级分类']").send_keys("BPC登录问题")
    #     self.driver.find_element(By.XPATH, "//*[text()='BPC登录问题']").click()
    #     self.driver.find_element(By.XPATH, "//*[@maxlength='200']").send_keys("selenium test" + order_name)
    #     logger.info(f"新增订单名称是:selenium test{order_name}")
    #     self.driver.find_element(By.CSS_SELECTOR, ".el-textarea__inner").send_keys("test test")
    #     self.driver.find_element(By.XPATH, "//*[text()='保存']").click()
    #
    #     from itsm.page.request_list_page import RequestListPage
    #     return RequestListPage(self.driver)



