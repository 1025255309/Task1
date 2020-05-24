"""
1.登录企业微信
2.获取登录cookie并存入cookie.json文件中
3.获取json文件打开企业微信，点击导入通信录
4.上传通信录excel文件
5.断言上传文件名称
"""
import json
import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAutologin():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(20)

    #@pytest.mark.skip
    def test_get_cookie(self):
        sleep(10)
        # print(self.driver.get_cookies())
        cookie = self.driver.get_cookies()  # 获取cookie
        with open("cookie.json","w") as f:
            #将cookie存放在一个json文件中
            json.dump(obj=cookie, fp=f)
        sleep(3)

    def test_cookie_login(self):
        # cookie是个元组，元组里面包含多个字典（典型的key-valu）
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852918021430'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'sp-ZxSJDlR4nue49JewN_4fkP2ZR4p-BeMdsUZ63i2oUNWol-YUV3ErmpVBBxLDCy1spF8f0PewZ9C-kCrHYxWNjtYK2bx7tsI_XUAY-4QINaSa7hwFCg5CHi_LhDOC4EGeLT6SkVjAl-R2dR1dkPAVC3XJohyY6JIcFTOIdH93AJwUjFN_I2nr4Lnt4lA98rgwt3sNPgPzBNz05dr5S8FQ4ViT32ZX-BliZFt1vJ9tIn3K41VJ1qKTZ2vKZDtwxyVZrQvHHS0651HiOmgSQng'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852918021430'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325016127066'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5148828'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': 'work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '2398839644'}, {'domain': '.qq.com', 'expiry': 1590291599, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1255989440.1590205188'}, {'domain': '.qq.com', 'expiry': 1590205248, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1653277199, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.587636549.1590205188'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1590205188'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '39483449462388564'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'xEeJLDPby_6nG9Fsho7r8Y_blLvEvKvI7lzpdIOi2WuNYEnsj9rm4tAQtf3d5fET'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1621741188, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1590205188'}, {'domain': '.work.weixin.qq.com', 'expiry': 1592797202, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
        # 通过json文件传入参数使用load（open()）
        cookies = json.load(open("./cookie.json"))

        # 循环遍历cookies列表，将所有cookie添加到浏览器中
        for cookie in cookies:
            # 注意一次只能添加一个cookie
            self.driver.add_cookie(cookie)
        sleep(3)  # cookie植入需要一定的时间
        # self.driver.refresh()  # 页面刷新
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click() # 注意是选这个父类的第二个儿子，且class前面需要加.
        #self.driver.find_element(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click() #不知道为啥不行
        # 选择上传文件，并添加文件的绝对路径，注意有ID的时候优先使用ID

        # self.driver.find_element(By.ID, "js_upload_file_input").send_keys("D:\proiect\单元测试demo\\test_selenium\cookie.xls")
        dir = os.path.dirname(__file__) # dir获取当前文件的绝对路径
        # 上传文件可以使用send_keys，但前提元素的标签必须为input
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(dir+"/cookie.xls")
        #获取上传文件name
        ele_name = self.driver.find_element(By.ID,"upload_file_name").text
        # 添加断言，断言上传文件的名称
        assert ele_name == "cookie.xls"





