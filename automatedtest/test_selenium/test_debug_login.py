"""
复用chrome浏览器
"""
from selenium import webdriver
# 注意此处的chrome小写
from selenium.webdriver.chrome.options import Options


class TestDebug:
    def test_debug_login(self):
        option=Options()
        option.debugger_address="localhost:9222"
        driver=webdriver.Chrome(options=option)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")