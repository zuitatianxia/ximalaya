import os,sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import BaseAction
class LoginPage(BaseAction):
    un_login_button=By.XPATH,"text,未登录"
    agree_button=By.XPATH,"text,同意,1"
    now_login_button=By.XPATH,"text,立即登录"
    password_login_button=By.XPATH,"text,密码登录"
    phone_number=By.XPATH,"text,请输入手机号"
    password_text_view = By.XPATH,"resource-id,com.ximalaya.ting.android:id/main_password"
    login_button=By.XPATH,"text,登录,1"
    succ_text=By.XPATH,"text,醉踏天下lwp,1"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        # 2、创建对象时 执行初始化方法 调用 同意许可 跳转页面方法
        self.click_agree()
        self.jump_to_login_page()
        #点击同意许可
    def click_agree(self):
        self.click(self.agree_button)
        #点击未登录 跳转到登录页面
    def jump_to_login_page(self):
        self.click(self.un_login_button)
        #点击 立即登录
    def click_now_login(self):
        self.click(self.now_login_button)
        #点击密码登录
    def password_login(self):
        self.click(self.password_login_button)
        #请输入手机号码
    def input_phone_number(self,text):
        self.input_search_text(self.phone_number,text)
        #点击密码框
    def click_password_text(self):
        self.click(self.password_text_view)
        #输入密码
    def input_password(self,text):
        self.input_search_text(self.password_text_view,text)
        #点击登录
    def click_login(self):
        self.click(self.login_button)
