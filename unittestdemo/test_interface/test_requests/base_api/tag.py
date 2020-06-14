import requests


from base_api.wework import WeWork

# 创建标签类（产品先的具体模块），继承自WeWork类，定义它的增删改查的方法
class Tag(WeWork):
    def create_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        params = {
            "access_token": self.token
        }
        json = {
            "tagname": "LZ",
            # "tagid": 12 # 标签id，非负整型，指定此参数时新增的标签会生成对应的标签id，不指定时则以目前最大的id自增。
        }
        r = requests.post(url=url, params=params, json=json)
        #print(r.json())
        return r.json()

    def update_tagname(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        params = {
            "access_token": self.token
        }
        json={
                "tagid": 9,
                #"tagname": "UI design2"
                "tagname": "HHHHH"
        }
        r= requests.post(url=url,params=params,json=json)
        return r.json()

    def delete_tag(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params = {
            "access_token": self.token,
            "tagid": 10
        }
        r=requests.get(url=url,params=params)
        return r.json()
