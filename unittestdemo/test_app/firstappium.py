# 运行测试用例:firstappium
# 。验证环境是否成功
# 。首先打开appium desktop，点击 start server，不报错
# 。其次准备一个android设备，真机或者模拟器，连接到电脑上并且通过adb devices查看设备是否连144115
# 。最后编写测试脚本，运行脚本
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(5)
driver.quit()

