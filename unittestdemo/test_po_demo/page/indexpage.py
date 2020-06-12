#
from test_po_demo.page.loginpage import LoginPage
from test_po_demo.page.registerpage import RegisterPage


class IndexPage:

    def goto_login(self):
        # 点击登录行为,进入登录页面
        # self.driver.find_element(By.ID,"xxx").click()
        return LoginPage()

    def goto_register(self):
        # 点击注册行为,进入注册页面
        # self.driver.find_element(By.ID,"xxx").click()
        return RegisterPage()

    def goto_download(self):
        pass