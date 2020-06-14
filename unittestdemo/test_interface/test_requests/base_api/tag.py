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

    def get_tagmember(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        params = {
            "access_token": self.token,
            "tagid": 3
        }
        r = requests.get(url=url, params=params)
        return r.json()

    def add_tagmember(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"
        params = {
            "access_token": self.token
        }
        # userlist、partylist不能同时为空，userlist单次请求个数不超过1000，partylist单次请求个数不超过100
        # 注意：userlist中如果是中文，则需要找对应的英文名字输入才可以，否则会返回'invalidlist'，企业微信更新不及时，可能会出现写对应的partylist，仍然报错'invalidparty'
        json={
                "tagid": 3,
                "userlist": ["YuanGong8","YuanGong9"],
                "partylist": [3,3]
        }
        r=requests.post(url=url, params=params, json=json)
        return r.json()

    def delete_tagmember(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers"
        params = {
            "access_token": self.token
        }
        json = {
            "tagid": 3,
            "userlist": ["YuanGong8", "YuanGong9"],
            "partylist": [3]
        }
        r = requests.post(url=url, params=params, json=json)
        return r.json()

    def get_taglist(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/list"
        params = {
            "access_token": self.token
        }
        r = requests.get(url=url, params=params)
        return r.json()

