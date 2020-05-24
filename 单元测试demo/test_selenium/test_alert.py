"""
alert窗口处理案例:
。打开网页 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
。操作窗口有侧页面，将元素1拖拽到元素2
。这时候会有一个alert弹框，点击弹框中的“确定”
。然后再按"点击运行”
。关闭网页
"""
import time

import pytest
from selenium.webdriver import ActionChains

from test_selenium.base import Base
class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        ele_drag=self.driver.find_element_by_id("draggable")
        ele_drop=self.driver.find_element_by_id("droppable")
        action=ActionChains(self.driver)
        action.drag_and_drop(ele_drag,ele_drop).perform()
        time.sleep(3)
        print("请点击alert确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath("submitBTN").click()
        time.sleep(3)