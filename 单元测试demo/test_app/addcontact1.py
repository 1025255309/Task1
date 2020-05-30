# 改造录制的用例：
# 第一次改造：修改定位方式，将自动生成的xpath绝对定位，修改为可阅读的，可维护的定位方式
# 使用appium录制企业微信添加成员的原生测试脚本，直接可以运行，但是存在的问题是使用xpath定位的元素，添加成员的位置变化了所以就报错，所以不推荐使用
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "mydevice"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.WwMainActivity"
caps["noReset"] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10) # 添加隐式等待，增加测试稳定性

# 点击通讯录
el1 = driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]')
el1.click()
# 点击添加成员，注意此处如果成员过多，一个页面显示不出来，需要使用滚动查找，这点不同于web页面，无论多长都能一次性刷新出来
#el2 = driver.find_element(MobileBy.XPATH,'//*[@text="添加成员"]')
el2 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                          'new UiSelector().scrollable(true).\
                          instance(0)).scrollIntoView(new UiSelector().\
                          text(“添加成员”).instance(0)')
el2.click()
# 点击手动输入添加，这里可以使用@text，也可以使用xpath提供的其他方法，比如contains,starts_with,ends_with等
#el3 = driver.find_element(MobileBy.XPATH,'//*[@text="手动输入添加"]')
#el3 = driver.find_element(MobileBy.XPATH,'//*[ends_with(@text,"输入添加")]')
#el3 = driver.find_element(MobileBy.XPATH,'//*[starts_with(@text,"手动输入")]')
el3 = driver.find_element(MobileBy.XPATH,'//*[contains(@text,"输入添加")]')
el3.click()

#定位姓名并输入
el4 = driver.find_element(MobileBy.XPATH,'//*[contains(@text,"姓名")]/..//*[@text="必填"]')
el4.send_keys("李四")
#定位姓别并点击选择对应的性别
el5 = driver.find_element(MobileBy.XPATH,'//*[contains(@text,"男")]')
el5.click()
el6 = driver.find_element(MobileBy.XPATH,'//*[contains(@text,"女")]')
el6.click()
#定位手机号并输入，使用@text定位手机会失败，原因是多了一个空格，在这种情况下一般就推荐使用contains
el7 = driver.find_element(MobileBy.XPATH,'//*[contains(@text,"手机号")]')
el7.send_keys("13800000004")
#定位并点击保存
el8 = driver.find_element(MobileBy.XPATH,'//*[@text="保存"]')
el8.click()

#加上断言
print(driver.page_source) # 打印当前页面
driver.find_element(MobileBy.XPATH,'//*[@text="添加成功"]')

#资源释放
driver.quit()