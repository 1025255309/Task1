"""
。测试案例一：test_click
。打开页面（http://sahitest.com/demo/clicks.htm）
。分别对按钮click me'，‘dbl click me'，right click me'，执行点击，双击，右键操作
。打印上面展示框中的内容

。测试案例二：
。移动到某个元素上,比如打开百度页面，
。action=ActionChains（self.driver）
。action.move_to_element（element）
。action.perform（）

比如百度页面搜索“selenium测试”，移动鼠标到最下面点击下一页
。测试案例四：
。打开网址：http://sahitest.com/demo/label.htm
。定位两个输入框e1，e2
。向输入框e1中输入文字‘username'
。使用全选，复制，粘贴到输入框e2中
"""
import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains


class TestFrame:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        action=ActionChains(self.driver)
        click=self.driver.find_element_by_css_selector("[value='click me']")
        #sleep(2)
        double_click=self.driver.find_element_by_css_selector("[value='dbl click me']")
        #sleep(2)
        right_click=self.driver.find_element_by_css_selector("[value='right click me']")
        action.click(click)
        action.double_click(double_click)
        action.context_click(right_click)
        action.perform()
        sleep(3)

    def test_move(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        self.driver.find_element_by_id("su").click()
        action=ActionChains(self.driver)
        down_element=
        action.move_to_element(ele)
        ##未完待续
