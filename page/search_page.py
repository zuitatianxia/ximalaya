import os,sys

from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from base.base_action import BaseAction
class SearchPage(BaseAction):
    #display_button = By.XPATH, "//*[contains(@text,'显示')]"
    display_button = By.XPATH, "text,显示"
    search_button = By.ID, "com.android.settings:id/search"
    sendkeys_button = By.ID, "android:id/search_src_text"
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    def click_display(self):
        self.click(self.display_button)

    def click_search(self):
        self.click(self.search_button)

    def input_content(self,text):
        self.input_search_text(self.search_button,text)

    def click_back(self):
        self.click(self.back_button)

