import os,sys

import allure
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from time import sleep
import pytest

from base.base_dirver import init_driver
from page.login_page import LoginPage
from base.base_yml import yml_data_with_file
from base.base_yml import data_with_key
class TestLogin:
    def setup(self):
        self.driver=init_driver()
        self.login_page=LoginPage(self.driver)
    #@pytest.mark.parametrize("args",data_with_key("test_login"))
    #@pytest.mark.parametrize(("username","password","toast"),data_with_key("test_login"))
    #def testlogin1(self,args):
    # def test_login(self,username,password,toast):
    #     #点击立即登录
    #     self.login_page.click_now_login()
    #     #点击 密码登录
    #     self.login_page.password_login()
    #     #5、输入手机号
    #     #self.login_page.input_phone_number(args[username])
    #     self.login_page.input_phone_number(username)
    #     #点击密码框
    #     self.login_page.click_password_text()
    #     #6、输入密码
    #     #self.login_page.input_password(args[password])
    #     self.login_page.input_password(password)
    #
    #     #7、点击登录
    #     self.login_page.click_login()
    #
    #     #断言登录是否成功
    #     #assert self.login_page.is_toast_exist(args[toast])
    #     # ele=self.login_page.is_toast_exist(toast)
    #     # print(ele)
    #     assert self.login_page.is_toast_exist(toast)
    #     # @pytest.mark.parametrize("args",data_with_key("test_login"))
    # #字典读取数据
    # @pytest.mark.parametrize("args",data_with_key("test_login1"))
    # def testlogin1(self,args):
    #     # 点击立即登录
    #     self.login_page.click_now_login()
    #     # 点击 密码登录
    #     self.login_page.password_login()
    #     # 5、输入手机号
    #     self.login_page.input_phone_number(args["username"])
    #     # 点击密码框
    #     self.login_page.click_password_text()
    #     # 6、输入密码
    #     self.login_page.input_password(args["password"])
    #     # 7、点击登录
    #     self.login_page.click_login()
    #
    #     # 断言登录是否成功
    #     assert self.login_page.is_toast_exist(args["toast"])
    #     # ele=self.login_page.is_toast_exist(toast)
    #     # print(ele)
    #指定测试数据顺序：
    @allure.step(title="测试登录脚本")
    @pytest.mark.parametrize("args", data_with_key("test_login2"))
    def test_login2(self, args):
        username=args['username']
        password=args['password']
        toast=args['toast']
        screen=args['screen_name']
        print(username,password,toast,screen)
        # 点击立即登录
        allure.attach("点击立即登录","立即登录按钮")
        self.login_page.click_now_login()
        # 点击 密码登录
        allure.attach("点击密码登录", "密码登录按钮")
        self.login_page.password_login()
        # 5、输入手机号
        allure.attach("输入手机号码", username)
        self.login_page.input_phone_number(username)
        # 点击密码框
        allure.attach("点击密码框", "点击密码框使其选中状态")
        self.login_page.click_password_text()
        # 6、输入密码
        allure.attach("输入密码", password)
        self.login_page.input_password(password)
        # 7、点击登录
        allure.attach("点击登录", "登录按钮")
        self.login_page.click_login()
        with open("./screen/"+screen+".png", "rb") as f:
            context = f.read()
        print("读取图片成功")
        # 断言登录是否成功
        allure.attach('断言 "判断对用提示"是否存在',toast)
        dy = self.login_page.is_toast_exist(toast, True, screen)
        #上传图片
        allure.attach(context, "图片" , attachment_type=allure.attachment_type.PNG)
        #print(dy)
        assert dy




