# -*- coding:utf-8 -*-
# author:jinzhu.hou
# datetime:2022/7/18 14:35
# software: PyCharm
import random
from time import sleep

import pytest
# from selenium.webdriver.common.by import By

from itsm.page.home_page import HomePage
from itsm.page.login_page import LoginPage
from itsm.page.request_list_page import RequestListPage


class TestItsm():
    def setup_class(self):
        self.home = LoginPage().login()


    def teardown_class(self):
        self.home.do_quit()

    num = str(random.randint(1, 9999))

    @pytest.mark.parametrize("name",[f"{num}"])
    def test_add1(self,name):
        list_page = self.home\
            .go_to_requestlist()\
            .go_to_newrequest()\
            .new_request(name)\
            .get_add_msg()


        assert list_page == "保存成功"

    def test_event(self):
        self.home.go_to_event().go_to_event_detail().assign_event()









