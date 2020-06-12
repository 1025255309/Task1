from appium.webdriver.common.mobileby import MobileBy

from test_app.page.base import BasePage


class ContactAddPage(BasePage):
    def set_name(self, username):
        # 定位姓名并输入
        el4 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]')
        el4.send_keys(username)
        return self

    def set_gendor(self, gendor):
        # 定位姓别并点击选择对应的性别
        el5 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"男")]')
        el5.click()
        self.driver.find_element(MobileBy.XPATH, f"//*[contains(@text,'{gendor}')]").click()
        return self

    def set_phonenum(self, phonenum):
        # 定位手机号并输入，使用@text定位手机会失败，原因是多了一个空格，在这种情况下一般就推荐使用contains
        el7 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机号")]')
        el7.send_keys(phonenum)
        return self

    def click_save(self):
        # 注意，这个python的一个机制，不允许循环导入，所以需要局部导入，也就是import locally
        from test_app.page.inviteadd import InviteAddPage
        # 定位并点击保存
        el8 = self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]')
        el8.click()

        return InviteAddPage(self.driver)
