'''
实战练习多窗口切换：
。打开百度页面
。点击登录，
。弹框中点击‘立即注册”，输入用户名和帐号
。返回刚才的登录页，点击登录。输入用户名和密码，点击登录
'''
import pytest
import selenium
from selenium import webdriver
from time import sleep
class TestWindows:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_window(self):
        self.driver.find_element_by_link_text("登录").click()
        # 点击立即注册之前获取当前窗口句柄和所有窗口句柄，目前只要一个窗口句柄即登录窗口
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        # 点击立即注册之后获取当前窗口句柄和所有窗口句柄
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        # 显然当前有两个窗口句柄（登录和注册），想要操作第二个窗口就需要使用switch_to_window（新窗口句柄）
        # 进行窗口切换，[-1]代表最后一个句柄（用于多个窗口），此时一直只有两个窗口则写[1]也是可以的
        handle_zc=self.driver.window_handles[-1]
        self.driver.switch_to.window(handle_zc)
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("password")
        # 此时在注册窗口，需要到登录页面操作，需要再次切换到注册窗口，[0]代表切回第一个窗口
        handle_dl=self.driver.window_handles[0]
        self.driver.switch_to.window(handle_dl)
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("13827422216")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("13827422216")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)


if __name__ == '__main__':
    pytest.main()
