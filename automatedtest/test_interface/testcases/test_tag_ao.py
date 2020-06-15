"""
此脚本是使用APIObject设计模式改造后的测试用例，里面只能看到测试用例实现逻辑和断言
"""
import yaml

from ..base_api.tag import Tag


class TestTagAo:

    def setup_class(self):  # token只需要每个用例集之前执行一次，不需要重复获取
        self.tag = Tag()
        self.token = self.tag.get_token(self.tag.yaml_load("config.yaml")["corpsecret"])

    # 测试用例只实现逻辑业务和断言
    def test_create_tag(self):
        r = self.tag.create_tag("QZ3",100)
        print(r)
        assert r["errcode"] == 0

    # @pytest.mark.skip
    def test_update_tagname(self):
        r = self.tag.update_tagname(9,"QZ2")
        print(r)
        assert r["errmsg"] == "updated"

    # @pytest.mark.skip
    def test_delete_tag(self):
        r = self.tag.delete_tag(100)
        assert r["errmsg"] == "deleted"

    # @pytest.mark.skip
    def test_get_tagmember(self):
        r = self.tag.get_tagmember(3)
        assert r["errcode"] == 0



    # @pytest.mark.skip
    def test_add_tagmember(self):
        r = self.tag.add_tagmember()
        assert r["errcode"] == 0

    # @pytest.mark.skip
    def test_delete_tagmember(self):
        r = self.tag.delete_tagmember()
        assert r["errcode"] == 0

    # @pytest.mark.skip
    def test_get_taglist(self):
        r = self.tag.get_taglist()
        assert r["errcode"] == 0
