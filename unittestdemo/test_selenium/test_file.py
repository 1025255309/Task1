"""
文件上传
"""
import time

import pytest

from test_selenium.base import Base
class TestFile(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        # 图片绝对路径，为防止特殊字符，每层路径都需要加上转义字符即可
        self.driver.find_element_by_id("stfile").send_keys("C:\\Users\\86138\\Desktop\\a.png")
        # 加强制等待时间
        time.sleep(3)
