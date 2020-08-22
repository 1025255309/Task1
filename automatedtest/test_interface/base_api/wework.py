"""
作业二：通讯录管理-标签管理接口，至少实现前四个（也就是作业一参考：test_tag.py）
1.使用apiobject 进行改造，分层
2.使用jsonpath， jsonschema，hamcrest这三个辅助断言工具，进行断言。
# 此脚本相对于实现base_api
"""


from test_interface.base_api.base_api import BaseApi
# 创建WeWork类（业务线）,继承于BaseApi类
class WeWork(BaseApi):
    def get_token(self,corpsecret):
        corpid = "ww2e51e84799d1f6f7"
        #corpsecret = "xMZ8h3PCTOGFp9TtjvWWfqtX--uwTdCPVcSmzRqRMn8"  #已使用yaml文件传参

        # 将requests请求信息改造成一个json结构体，刚好regusets.request方式的参数（method,url,**kwargs），完成了requests解耦
        req = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }
        r = self.send_api(req)
        #r = requests.get(url=url, params=param)
        # print(type(r.json())) 查看r.token是一个字典类型
        self.token = r["access_token"]
        return self.token
