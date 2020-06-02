import pytest
from appium.webdriver.common.mobileby import MobileBy

from test_app.page.base import BasePage
from test_app.page.workweixin import App


class TestContact():
    def setup(self):
        self.app = App()
        pass
    @pytest.mark.parametrize('username,gendor,phonenum',[
        # ("员工5", "男", "13300000004"),
        # ("员工6", "女", "13300000005"),
        # ("员工7", "男", "13300000006"),
        ("员工10", "男", "13300000010")
    ])
    def test_addmember(self,username,gendor,phonenum):

        self.app.start().main().goto_contact().addmember().manualadd().set_name(username).set_gendor(gendor).set_phonenum(phonenum).click_save()

        # # 加上断言
        # print(self.driver.page_source)  # 打印当前页面
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')