"""
复用浏览器：实现自动化登录企业微信，一般用于调试
"""

from time import sleep

from selenium import webdriver
# 注意是小写的chrome
from selenium.webdriver.chrome.options import Options

class TestLogin:
    def test_debug_login(self):
        # 实例化一个option，并调用它的debugger_address打开复用浏览器
        option = Options()
        # 启动本地的一个服务，注意options.add_experimental_option ("debuggerAddress", "127.0.0.1:9222")格式是：ip:port(即：hostname[:port])
        option.debugger_address = "localhost:9222/"
        # 通过本地服务的debugger_address可以直接控制浏览器，注意一定要传参，通过options传入，如果不传也可以运行成功，但需要登录，无法直接跳转到指定的页面，
        driver = webdriver.Chrome(options=option)
        # driver.get("https://work.weixin.qq.com/")
        # 进去企业微信，不用每次都扫码登录了
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
