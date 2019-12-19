import os, sys
sys.path.append(os.getcwd())
import random
import pytest
from time import sleep
from appium import webdriver
from base.base_dirver import init_driver
from page.network_page import NetworkPage
class TestNetwork:
    def setup(self):
        self.driver=init_driver()
        self.network_page=NetworkPage(self.driver)
    def test_mobile_network_2g(self):
        # self.network_page.click_more()
        # self.network_page.click_neteork()
        # self.network_page.click_firstnetwork()
        self.network_page.click_2G()
    def test_mobile_network_3g(self):
        # self.network_page.click_more()
        # self.network_page.click_neteork()
        # self.network_page.click_firstnetwork()
        self.network_page.click_3G()