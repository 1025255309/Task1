from test_po_demo.page.registerpage import RegisterPage


class LoginPage:

    def scanf_login(self):
        pass

    def goto_register(self):
        # 点击注册行为,进入注册页面
        # self.driver.find_element(By.ID,"xxx").click()
        return RegisterPage()
