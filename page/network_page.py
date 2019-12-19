from time import sleep
from base.base_action import BaseAction
from selenium.webdriver.common.by import By

class NetworkPage(BaseAction):

    #更多按钮
    more_button=By.XPATH,"//*[contains(@text,'更多')]"
    #移动网络按钮
    network_button=By.XPATH,"//*[contains(@text,'移动网络')]"
    #首选网络按钮
    firstnetwork_button=By.XPATH,"//*[contains(@text,'首选网络类型')]"
    #2G按钮
    click2G_button=By.XPATH,"//*[contains(@text,'2G')]"
    #3G按钮
    click3G_button=By.XPATH,"//*[contains(@text,'3G')]"

    #初始化方法，创建方法时 执行内部方法(分别点击 更多 移动网络 首选网络 )
    def __init__(self,driver):
        #self.driver=driver
        BaseAction.__init__(self,driver)
        self.click_more()
        self.click_neteork()
        self.click_firstnetwork()

    def click_more(self):
        #self.find_element(self.more_button).click()
        self.click(self.more_button)

    def click_neteork(self):
        #self.find_element(self.network_button).click()
        self.click(self.network_button)

    def click_firstnetwork(self):
        #self.find_element(self.firstnetwork).click()
        self.click(self.firstnetwork_button)

    def click_2G(self):
        #self.find_element(self.click2G_button).click()
        self.click(self.click2G_button)

    def click_3G(self):
        #self.find_element(self.click3G_button).click()
        self.click(self.click3G_button)

    #自定义函数
    # def find_element(self,loc):
    #     return self.driver.find_element(loc[0],loc[1])