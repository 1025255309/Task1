"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestXpath:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
    def teardown(self):
        self.driver.quit()
    def test_search(self):
        #self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        #self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
        #self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR,'[id=kw]').send_keys("霍格沃兹测试学院")
        #self.driver.find_element_by_id("su").click()
        self.driver.find_element(By.ID,"su").click()
        self.driver.find_element(By.ID, "su").screenshot()


