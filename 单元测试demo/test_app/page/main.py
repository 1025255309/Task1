from test_app.page.base import BasePage
from test_app.page.contact import ContactListPage
from appium.webdriver.common.mobileby import MobileBy

class Main(BasePage):
    def goto_message(self):
        pass
    def goto_contact(self):
        # 点击通讯录
        el1 = self._driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]')
        el1.click()
        return ContactListPage()
    def goto_workbench(self):
        pass
    def goto_profile(self):
        pass


