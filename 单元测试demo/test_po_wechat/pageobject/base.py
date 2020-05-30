from selenium import webdriver
from selenium.webdriver.common.by import By

class Base:
    def base(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(20)
        #self.driver.find_element(By.ID,)