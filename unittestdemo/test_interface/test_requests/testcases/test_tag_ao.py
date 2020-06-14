import requests
from base_api.tag import Tag
from base_api.wework import WeWork


class TestTagAo:
    def setup(self):
        self.tag=Tag()
        self.token=self.tag.get_token()

    # 测试用例只实现逻辑业务和断言
    def test_create_tag(self):
        r=self.tag.create_tag()
        print(r)
        assert r["errcode"] == 0

    #@pytest.mark.skip
    def test_update_tagname(self):
        r=self.tag.update_tagname()
        print(r)
        assert r["errmsg"] == "updated"

    #@pytest.mark.skip
    def test_delete_tag(self):
        r=self.tag.delete_tag()
        assert r.json()["errmsg"] == "deleted"

    #@pytest.mark.skip
    def test_get_tagmember(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        params = {
            "access_token": self.token,
            "tagid": 3
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    #@pytest.mark.skip
    def test_add_tagmember(self):
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
        print(r.json())
        assert r.json()["errcode"] == 0

    #@pytest.mark.skip
    def test_delete_tagmember(self):
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
        print(r.json())
        assert r.json()["errcode"] == 0

    #@pytest.mark.skip
    def test_get_taglist(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/tag/list"
        params = {
            "access_token": self.token
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0