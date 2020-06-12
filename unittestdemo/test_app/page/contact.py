from test_app.page.base import BasePage
from test_app.page.inviteadd import InviteAddPage
from appium.webdriver.common.mobileby import MobileBy

class ContactListPage(BasePage):
    def addmember(self):
        # 点击添加成员，注意此处如果成员过多，一个页面显示不出来，需要使用滚动查找，这点不同于web页面，无论多长都能一次性刷新出来
        # el2 = self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]')
        el2 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().\
                                        scrollable(true).instance(0)).\
                                        scrollIntoView(new UiSelector().\
                                        text("添加成员").instance(0));')
        el2.click()
        return InviteAddPage(self.driver)
    def selectmember(self):
        pass


    def delmember(self):
        pass
