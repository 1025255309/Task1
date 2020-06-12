"""
selenium中如何调用js：
js处理-案例1-滑动
。场景：页面显示的数据比较多，需要点击底部的对象，我们就需要把鼠标移动到底部，才可以点击对象
。案例一：滑动到浏览器底部或者顶部
。打开百度首页
。输入搜索关键字，
。点击搜索后，跳转到搜索结果页
。滑动到底部点击’下一页
"""
import time

import pytest

from test_selenium.base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # 需要返回的话，一定要加上return
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        ele_scroll = self.driver.execute_script("return document.documentElement.scrollTop=10000")
        time.sleep(3)

        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()

        time.sleep(3)
        # # JSON.stringify(performance.timing)获取当前页的性能参数，需要返回值，就要加上return
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        #第二种方式也是可以直接打印
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

"""
js处理-案例2-时间控件
。大部分时间控件都是readonly属性，需要手动去选择对应的时间，手工测试中很容易做到，自动化中对控件的操作可以使用js来操作。
。处理时间控件思路：
。1.要取消日期的readonly属性
。2.给value赋值
。写js代码来实现如上的1，2点，再webdriver对js进行处理
。测试案例三：
。打开网址https://www.12306.cn/index/
。修改出发日期为2020-12-30
。打印出发日期
。关闭网址
"""
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("document.getElementById('train_date')")
        self.driver.execute_script("ele_time=document.getElementById('train_date')")
        self.driver.execute_script("ele_time.removeAttribute('readonly')")
        time.sleep(2)
        self.driver.execute_script("ele_time.value='2020-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return ele_time.value"))
