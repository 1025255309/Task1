"""
表单操作实例：表单使用表单标签（<form>）定义。例如：<form><input/></form>
1.打开https://testerhome.com/account/sign_in
2.输入账号，密码
3.选择记住密码
4.点击登录
"""
from time import sleep

import pytest
from selenium import webdriver


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_xpath("//*[@id='user_login']").send_keys("520lxf")
        self.driver.find_element_by_xpath("//*[@id='user_password']").send_keys("1025255309lxf")
        self.driver.find_element_by_xpath("//*[@id='user_remember_me']").click()
        self.driver.find_element_by_name("commit").click()
        sleep(5)

if __name__ == '__main__':
    pytest.main()