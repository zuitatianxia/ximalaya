import os,sys
sys.path.append(os.getcwd())
import pytest
from base.base_dirver import init_driver
from page.search_page import SearchPage
from base.base_yml import yml_data_with_file
def data_with_key(key):
    data=yml_data_with_file("search_data")[key]
    return data
class TestSearch:
    def setup(self):
        self.driver=init_driver()
        self.search_page=SearchPage(self.driver)
    @pytest.mark.parametrize("content",data_with_key("test_search"))
    def test_search(self,content):
        # #点击显示
        self.search_page.click_display()
        #点击放大镜
        self.search_page.click_search()
        #输入文字
        self.search_page.input_content(content)
        #点击返回
        self.search_page.click_back()

    @pytest.mark.parametrize("content", data_with_key("test_search1"))
    def test_search1(self,content):
        # #点击显示
        # self.search_page.click_display()
        #点击放大镜
        self.search_page.click_search()
        #输入文字
        self.search_page.input_content(content)
        #点击返回
        self.search_page.click_back()