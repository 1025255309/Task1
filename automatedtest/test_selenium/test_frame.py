"""
实战练习：
。多frame切换案例：
。打开包含frame的web页面
https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
。打印“请拖拽我’元素的文本
。打印”点击运行“元素的文本
"""
import pytest
from selenium import webdriver
from time import sleep
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
        # self.driver.switch_to_frame("iframeResult")这是第二种切换方式，通常我们使用第一种
        # 打印text属性需要使用.text获取属性
        print(self.driver.find_element_by_id("draggable").text)
        print(self.driver.find_element_by_id("droppable").text)
        self.driver.switch_to.default_content()  # 切换到默认frame，第一种方式
        #self.driver.switch_to.parent_frame()  # 切换到父frame第二种方式，两种方式都可以
        print(self.driver.find_element_by_id("submitBTN").text)



if __name__ == '__main__':
     pytest.main()
