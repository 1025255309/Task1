"""
作业二：通讯录管理-标签管理接口，至少实现前四个（也就是作业一参考：test_tag.py）
1.使用apiobject 进行改造，分层
2.使用jsonpath， jsonschema，hamcrest这三个辅助断言工具，进行断言。
# 此脚本相对于实现base_api
"""
import requests



from test_interface.base_api.base_api import BaseApi

# 创建WeWork类（业务线）,继承于BaseApi类
class WeWork(BaseApi):
    def get_token(self,corpsecret):
        corpid = "ww2e51e84799d1f6f7"
        #corpsecret = "xMZ8h3PCTOGFp9TtjvWWfqtX--uwTdCPVcSmzRqRMn8"
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url=url, params=param)
        # print(type(r.json())) 查看r.token是一个字典类型
        self.token = r.json()["access_token"]
        return self.token
