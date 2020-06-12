"""
提交表单实例：登录百度账号
。打开百度页面
。点击登录，
。弹框中点击‘立即注册”，输入用户名和帐号
。返回刚才的登录页，点击登录。输入用户名和密码，点击登录
"""
from time import sleep

import pytest

from test_selenium.base import Base

# 定义一个类，继承于Base，所以在测试用例执行之前会先执行Base中的setup方法，执行完最后执行teardown方法
class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        # self.driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[3]/a").click()
        windows = self.driver.window_handles
        print(self.driver.window_handles)
        self.driver.switch_to.window(windows[-1])
        #self.driver.find_element_by_link_text("用户名").send_keys("username")
        #self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_4__userName']").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        sleep(3)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__footerULoginBtn']").click()
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__userName']").send_keys("13827422216")
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__password']").send_keys("1025255309lxf")
        self.driver.find_element_by_link_text("登录").click()
        sleep(3)

if __name__ == '__main__':
    pytest.main("-v")



