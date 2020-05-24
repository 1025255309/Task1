"""
三种等待：
1.强制等待，time.sleep(3)一般调试使用，实际自动化测试中不推荐使用
2.隐式等待，是全局变量，一般在初始化方法中定义，self.driver.impilicitly_wait(10)
3.显示等待：
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        # # 设置隐式全局等待
        # self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="归入各种类别的所有主题"]/a').click()  # 找到元素分类并点击
        # sleep(3)  # 设置强制等待

        # def wait(x):  # 这里为显示等待的until定义一个方法，并传一个参数x，x无实际意义，但是必须要有
        #     # 判断如果元素"最新"出现大于等于一次，就执行until后面的语句，否则循环检查，知道检测时间超过设置的显式等待时间会返回timeout
        #     return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1  # 注意此处是elements
        # # 导入显示等待，并使用until条件判断,注意until的用法,需要传入一个方法，这个方法必须有参数，所以我们上面定义一个wait(x)方法
        # WebDriverWait(self.driver, 10).until(wait)  # 注意传入方法时不加括号，加了括号代表调用函数

        # 上面显式等待的方式在selenium已经集成，我们可以使用内置的条件expected_conditions其中的一个方法
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()  # 找到元素热门并点击



