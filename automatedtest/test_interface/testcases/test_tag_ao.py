"""
此脚本是使用APIObject设计模式改造后的测试用例，里面只能看到测试用例实现逻辑和断言
使用jsonpath断言
"""
import json

from jsonpath import jsonpath
import yaml
from test_interface.base_api.tag import Tag
from hamcrest import *


class TestTagAo:

    def setup_class(self):  # token只需要每个用例集之前执行一次，不需要重复获取
        self.tag = Tag()
        self.token = self.tag.get_token(self.tag.yaml_load("config.yaml")["corpsecret"])

    # 测试用例只实现逻辑业务和断言
    def test_create_tag(self):
        r = self.tag.create_tag("QZ5",102)
        print(r)
        assert r["errcode"] == 0

    # @pytest.mark.skip
    def test_update_tagname(self):
        r = self.tag.update_tagname(102,"QZ8")
        print(r)
        assert r["errmsg"] == "updated"

    # @pytest.mark.skip
    def test_delete_tag(self):
        r = self.tag.delete_tag(102)
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
        # json的格式化工具，打印带格式，好看.
        # print(json.dumps(r,indent=2,ensure_ascii=False))
        print(jsonpath(r,"$.taglist[?(@.tagid == 100)]"))  #注意导入jsonpath一定要按这个格式，否则会报错：from jsonpath import jsonpath
        print(jsonpath(r, "$.taglist[?(@.tagid == 100)]")[0]["tagname"])
        res=jsonpath(r, "$.taglist[?(@.tagid == 100)]")[0]["tagname"]
        assert r["errcode"] == 0
        #assert res == "QZ3"
        assert_that(res,equal_to("QZ3"),reason="匹配失败")  #hamcrest就是assert_that(actual, matcher=None, reason="") 实际值，匹配值，如果不匹配会弹出的报错信息
        # res = jsonpath(r, "$.taglist[?(@.tagid == 100)]")[0]
        # assert_that(res, has_value("QZ3"), reason="匹配失败")  #可以自己多练习其他的

