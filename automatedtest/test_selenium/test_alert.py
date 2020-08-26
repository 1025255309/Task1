"""
实战练习：
1.打开网页
https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
2.操作窗口右侧页面，将元素1拖拽到元素2
3.这时候会有一个alert弹框，点击弹框中的‘确定’
3.然后再按’点击运行’
4.关闭网页
"""
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
class TestFrame:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_frame(self):
        # 检查要打印的元素，可以发现他们属于iframe元素，也就是需要先使用switch_to.frame("新frame的id")切换到对应的frame页
        self.driver.switch_to.frame("iframeResult")
        # 拖拽需要调用ActionChains方法
        action=ActionChains(self.driver)
        drag=self.driver.find_element_by_id("draggable")
        drop=self.driver.find_element_by_id("droppable")
        action.drag_and_drop(drag,drop).perform()
        sleep(2)
        # 拖拽完成后会弹出一个alert弹框，所以需要切换到alert,并调用.accept()进行确认操作
        self.driver.switch_to.alert.accept()
        # 点击确认后，alert弹框消失，默认还是在拖拽的iframe页面，接下来要点击运行，所以要再次进行切换
        self.driver.switch_to.default_content()  # 切换到默认frame，第一种方式
        #self.driver.switch_to.parent_frame()  # 切换到父frame第二种方式，两种方式都可以
        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
if __name__ == '__main__':
     pytest.main()
