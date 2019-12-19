from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_dirver import init_driver
from until.xpath_until import XpathUntil
class BaseAction:

    def __init__(self,driver):
        self.driver=driver

    #函数3 输入文本自定义函数 调用函数1
    def input_search_text(self,loc,text):
        self.find_elenent(loc).send_keys(text)

    #自定义函数2（调用函数1）
    def click(self,loc):
        self.find_elenent(loc).click()

    #自定义函数1
    def find_elenent(self,loc,timeout=20,poll=1.0):
        by=loc[0]
        value=loc[1]
        if by==By.XPATH:
            value=XpathUntil().make_xpath_feature(value)
            print(value)
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(by,value))

    def find_toast(self, message, is_screenshot=False,screenshot_name=None, timeout=15,poll=0.1):
        """
        # message: 预期要获取的toast的部分消息
        """
        message = "//*[contains(@text,'" + message + "')]"  # 使用包含的方式定位
        element=self.find_elenent((By.XPATH,message),timeout,poll)
        #element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(By.XPATH, message))
        if is_screenshot ==True:
            self.screenshot(screenshot_name)
            print("截图提示")
        return element.text

    def is_toast_exist(self, message, is_screenshot=False,screenshot_name=None, timeout=15, poll=0.05):
        # toa=self.find_toast(message, is_screenshot, screenshot_name, timeout, poll)
        # return toa
        try:
            self.find_toast(message, is_screenshot,screenshot_name,timeout, poll)
            return True
        except Exception:
            return False
    def screenshot(self,file_name):
        self.driver.get_screenshot_as_file("./screen/"+file_name+".png")
