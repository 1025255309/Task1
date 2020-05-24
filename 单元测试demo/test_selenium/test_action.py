"""
动作链接ActionChains用法实例：

"""
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

"""
。测试案例一：
。打开页面（http://sahitest.com/demo/clicks.htm）
。分别对按钮click me'，‘dbl click me'，right click me'，执行点击，双击，右键操作
。打印上面展示框中的内容
"""
    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        #element_click = self.driver.find_element(By.XPATH,"//*/html/body/form/input[3]")
        #element_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_elements_by_xpath("/html/body/form/input[2]")
        #element_rightclick = self.driver.find_elements_by_xpath("/html/body/form/input[4]")
        action = ActionChains(self.driver)  # ?????
        action.click(element_click)
        action.double_click(element_doubleclick)
        #action.context_click(element_rightclick)
        sleep(3)
        action.perform()
        sleep(3)

"""
测试案例二：鼠标移动到某个元素上
"""

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com")
        #ele = self.driver.find_element_by_link_text("设置")  #为啥这个是错的？
        ele = self.driver.find_element_by_link_text("更多")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

"""
测试案例三：将元素从位置A拖拽到位置B
"""
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        element_drag = self.driver.find_element_by_id("dragger")
        element_drop = self.driver.find_element_by_xpath("/html/body/div[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(element_drag, element_drop).perform()
        # action.click_and_hold(element_drag).move_to_element(element_drop).release().perform()
        # action.click_and_hold(element_drag).release(element_drop).perform()
        sleep(3)

"""
。测试案例四：
。打开网址：http://sahitest.com/demo/label.htm
。定位两个输入框e1，e2
。向输入框e1中输入文字‘username'
。使用全选，复制，粘贴到输入框e2中
"""

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele=self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action=ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("Tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)
        action.perform()
        sleep(3)




if __name__ == '__main__':
    pytest.main("-v")
