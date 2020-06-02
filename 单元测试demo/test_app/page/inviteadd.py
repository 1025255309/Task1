from test_app.page.base import BasePage
from test_app.page.contactadd import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy

class InviteAddPage(BasePage):
    def manualadd(self):
        # 点击手动输入添加，这里可以使用@text，也可以使用xpath提供的其他方法，比如contains,starts_with,ends_with等
        el3 = self._driver.find_element(MobileBy.XPATH, '//*[contains(@text,"输入添加")]')
        el3.click()
        return ContactAddPage()