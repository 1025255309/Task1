"""
TouchActions手势控制用法的实例：
·打开Chrome
·打开URL:http://www.baidu.com
。向搜索框中输入'selenium测试'
。通过TouchAction点击搜索框
。滑动到底部，点击下一页
。关闭Chrome
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouch:
    def setup(self):
        # 以下两条指令用于解决报错：unknown command:Cannot call non M3C standard command while in w3C mode
        option=webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        self.driver.get("http://www.baidu.com")
        ele=self.driver.find_element_by_id("kw")
        ele_touch=self.driver.find_element_by_id("su")
        ele.send_keys("selenium测试")
        ele_touch.click()
        #sleep(3)
        touchaction=TouchActions(self.driver)
        touchaction.tap(ele)
        touchaction.perform()
        touchaction.scroll_from_element(ele, 0, 10000).perform()
        sleep(3)

# 定义入口函数
if __name__ == '__main__':
    pytest.main("-v")