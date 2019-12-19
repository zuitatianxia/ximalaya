from time import sleep
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class DisplayPage(BaseAction):
    display_button=By.XPATH,"//*[contains(@text,'显示')]"
    search_button=By.ID,"com.android.settings:id/search"
    sendkeys_button=By.ID,"android:id/search_src_text"
    back_button=By.CLASS_NAME,"android.widget.ImageButton"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        # self.driver=driver
        # # 点击显示
        self.click_display()

    def click_display(self):
        #self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        #self.find_element(self.display_button).click()
        self.click(self.display_button)

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        #self.find_element(self.search_button).click()
        self.click(self.search_button)

    def input_text(self,text):
        #self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        #self.find_element(self.sendkeys_button).send_keys(text)
        self.input_search_text(self.sendkeys_button,text)

    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        #self.find_element(self.back_button).click()
        self.click(self.back_button)

    #自定义函数
    # def find_element(self,loc):
    #     return self.driver.find_element(loc[0],loc[1])