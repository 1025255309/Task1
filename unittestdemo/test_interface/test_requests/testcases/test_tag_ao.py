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
        r=self.tag.get_tagmember()
        assert r["errcode"] == 0

    #@pytest.mark.skip
    def test_add_tagmember(self):
        r=self.tag.add_tagmember()
        assert r.json()["errcode"] == 0

    #@pytest.mark.skip
    def test_delete_tagmember(self):
        r=self.tag.delete_tagmember()
        assert r.json()["errcode"] == 0

    #@pytest.mark.skip
    def test_get_taglist(self):
        r=self.tag.get_taglist()
        assert r.json()["errcode"] == 0