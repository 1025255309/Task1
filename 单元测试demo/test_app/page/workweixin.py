from appium.webdriver.webdriver import WebDriver

from test_app.page.base import BasePage
from test_app.page.main import Main
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class App(BasePage):
    driver: WebDriver
    def start(self):
        # 加上判断就可以复用启动
        if self._driver == None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps["appPackage"] = "com.tencent.wework"
            desired_caps["appActivity"] = ".launch.WwMainActivity"
            desired_caps['noReset'] = True
            # desired_caps['dontStopAppOnReset'] = True
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self.driver.launch_app()  # driver.launch_app默认会启动desired_capabalities中设定的应用

        self.driver.implicitly_wait(10)
        return self
    def restart(self):
        pass

    def stop(self):
        self.driver.quit()

    def main(self) -> Main:  # 类型提示
        return Main(self.driver)