import pytest
import requests

class TestTag:

    def setup(self):
        corpid = "ww2e51e84799d1f6f7"
        corpsecret = "xMZ8h3PCTOGFp9TtjvWWfqtX--uwTdCPVcSmzRqRMn8"
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url=url, params=param)
        # print(type(r.json())) 查看r.token是一个字典类型
        self.token = r.json()["access_token"]

    @pytest.mark.skip
    def test_create_tag(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        params={
            "access_token":self.token
        }
        json={
           "tagname": "BL",
           # "tagid": 12 # 标签id，非负整型，指定此参数时新增的标签会生成对应的标签id，不指定时则以目前最大的id自增。
        }
        r=requests.post(url=url,params=params,json=json)
        print(r.json())
        assert r.json()["errcode"] == 0
    @pytest.mark.skip
    def test_update_tagname(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        params = {
            "access_token": self.token
        }
        json={
                "tagid": 1,
                "tagname": "UI design"
        }
        r= requests.post(url=url,params=params,json=json)
        print(r.json())
        assert r.json()["errmsg"] == "updated"

    @pytest.mark.skip
    def test_delete_tag(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params = {
            "access_token": self.token,
            "tagid": 1
        }
        r=requests.get(url=url,params=params)
        print(r.json())
        assert r.json()["errmsg"] == "deleted"

    @pytest.mark.skip
    def test_get_tagmember(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        params = {
            "access_token": self.token,
            "tagid": 3
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    def test_add_tagmember(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"
        params = {
            "access_token": self.token
        }
        # userlist、partylist不能同时为空，单次请求个数不超过100
        json={
                "tagid": 1,
                "userlist":
                "partylist": 3
        }
        r=requests.post(url=url,params=params,json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    def test_delete_tagmember(self):
        pass
    def test_get_taglist(self):
        pass

