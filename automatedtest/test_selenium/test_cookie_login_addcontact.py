import json
import os
from time import sleep

from selenium import webdriver


class TestCookie:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    def test_get_cookie(self):
        sleep(6)
        self.driver.refresh()
        # driver.get_cookies()获取cookie
        cookie=self.driver.get_cookies()
        # 将cookie保存到cookie.json文件中，注意要使用json.dump()
        with open("cookie.json","w") as f:
            json.dump(cookie,f)


    def test_cookie_login_addcontact(self):
        #cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688852918021430'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'ZFSaLUdXuNdgFhBWNqBpSdkN7-AjJhh7wx9jOzA9BA-18-WNt-nBJnPclEiV3bKCnZ3OVtd4ZLjgPBcPQSonsOj-HxXbOqswKU_3LwV2iWOUAckRa0bMl3g2WxkTy1eyBQjlFJU3ChlVfUWrRHY3vsK40nTvmeqsamzbjLkp7VcpDEgnYD66MPCw6_mFZbO4xfymIir0BRhXcRAkC_jSuK2R36wtP_CEicL2ZjOa5CaXgkvs-1d7oEcoCFHymgzqANHJ29c3GjDxuiSQ85cCfA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688852918021430'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325016127066'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6986308'}, {'domain': '.qq.com', 'expiry': 1598412188, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2124018994.1598325788'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598357323, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '3iv4mu3'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '27380145771387952'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'xEeJLDPby_6nG9Fsho7r8XNa8o6RTm9F5CqzGs5t52wGGL3s6EEuGMuDF6vs8Nt2'}, {'domain': '.qq.com', 'expiry': 1598325848, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1661397788, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1706369456.1598325788'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629861787, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600917794, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        # 获取当前文件目录的固定用法，(__file__)代表当前文件
        dir=os.path.dirname(__file__)
        # print(os.path.dirname(__file__))
        #print(__file__)
        # 使用json.load(open())加载cookie传入
        cookies=json.load(open(dir+"\cookie.json"))
        # 此处要注意，一个页面的cookie有好多个，但是add_cookie方法一次只能加入一个cookie，所以此处需要使用for循环遍历添加
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        sleep(3)
        self.driver.refresh()
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        sleep(3)
        self.driver.find_element_by_id("js_upload_file_input").send_keys(dir+"/data.xlsx")
        ele_file=self.driver.find_element_by_id("upload_file_name")
        assert ele_file.text == "data.xlsx"
