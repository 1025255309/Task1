"""
企业微信接口自动化测试实战----获取access_token，参考：https://work.weixin.qq.com/api/doc/10013#%E6%9C%AF%E8%AF%AD%E4%BB%8B%E7%BB%8D
第三步：获取access_token
请求方式：GET（HTTPS）
请求URL：https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
注：此处标注大写的单词ID和SECRET，为需要替换的变量，根据实际获取值更新。其它接口也采用相同的标注，不再说明。
参数	        必须	     说明
corpid	    是	    企业ID
corpsecret	是	应用的凭证密钥
推荐使用第二种test_token_param传参方式编写
"""

import requests
class TestToken:

    def test_token(self):
        corpid = "ww2e51e84799d1f6f7"
        corpsecret = "xMZ8h3PCTOGFp9TtjvWWfqtX--uwTdCPVcSmzRqRMn8"
        # 使用f可以直接引用参数
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        # 使用json获取它的响应体
        print(r.json())

    def test_token_param(self):
        corpid = "ww2e51e84799d1f6f7"
        corpsecret = "xMZ8h3PCTOGFp9TtjvWWfqtX--uwTdCPVcSmzRqRMn8"
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url=url, params=param)
        print(r.json())
