"""
。文件上传实站测试案例：
。打开百度图片网址：https://image.baidu.com
。识别上传按钮
。点击上传按钮
。将本地的图片文件上传
"""
import pytest
import selenium
from selenium import webdriver
from time import sleep
class TestWindows:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_file(self):
        # 首先查找相机📷样式元素进行点击，进入选择图片界面
        self.driver.find_element_by_xpath("//*[@id='form']/span[1]/span[1]").click()
        # 强制等待看效果
        sleep(2)
        # 查找选择图片可以发现是input标签，所以可以直接调用send_keys方法上传
        self.driver.find_element_by_xpath("//*[@id='form']/div/div[2]/div[2]/input").\
            send_keys("D:\\proiect\\automatedtest\\test_selenium\\baidu.png")
        sleep(3)

if __name__ == '__main__':
    pytest.main()

