"""
第二次改造：使用pytest 测试框架(基于addcontact1.py)


"""
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class TestContact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps["appPackage"] = "com.tencent.wework"
        desired_caps["appActivity"] = ".launch.WwMainActivity"
        desired_caps['noReset'] = True
        #desired_caps['dontStopAppOnReset'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('username,gendor,phonenum',[
        ("员工5", "男", "13300000004"),
        ("员工6", "女", "13300000005"),
        ("员工7", "男", "13300000006"),
        ("员工9", "男", "13300000008")
    ])
    def test_addmember(self,username,gendor,phonenum):
        # 点击通讯录
        el1 = self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]')
        el1.click()
        # 点击添加成员，注意此处如果成员过多，一个页面显示不出来，需要使用滚动查找，这点不同于web页面，无论多长都能一次性刷新出来
        # el2 = self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]')
        el2 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                       'new UiScrollable(new UiSelector().\
                                        scrollable(true).instance(0)).\
                                        scrollIntoView(new UiSelector().\
                                        text("添加成员").instance(0));')
        el2.click()
        # 点击手动输入添加，这里可以使用@text，也可以使用xpath提供的其他方法，比如contains,starts_with,ends_with等
        # el3 = self.driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]')
        # el3 = self.driver.find_element(MobileBy.XPATH,'//*[ends_with(@text,"输入添加")]')
        # el3 = self.driver.find_element(MobileBy.XPATH,'//*[starts_with(@text,"手动输入")]')
        el3 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"输入添加")]')
        el3.click()

        # 定位姓名并输入
        el4 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"姓名")]/..//*[@text="必填"]')
        el4.send_keys(username)
        # 定位姓别并点击选择对应的性别
        # gendor = '女'
        el5 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"男")]')
        el5.click()
        self.driver.find_element(MobileBy.XPATH,f"//*[contains(@text,'{gendor}')]").click()

        # el6 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"女")]')
        # el6.click(gendor)
        # 定位手机号并输入，使用@text定位手机会失败，原因是多了一个空格，在这种情况下一般就推荐使用contains
        el7 = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机号")]')
        el7.send_keys(phonenum)
        # 定位并点击保存
        el8 = self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]')
        el8.click()

        # 加上断言
        print(self.driver.page_source)  # 打印当前页面
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')

if __name__ == '__main__':
    pytest.main()