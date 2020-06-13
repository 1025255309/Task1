"""
企业微信接口测试实战
❖ 获取access_token：使用test_param.py获取taken方式
❖ 增删查改：课堂练习部门管理，分别实现创建部门，更新部门，删除部门，获取部门列表的测试用例
❖ 参考https://work.weixin.qq.com/api/doc/90000/90135/90930
要学会查看企业微信API文档，第一步看请求方式，第二步填充参数，
一般get请求需要传三个参数（url,params,json响应体），post请求需要传两个参数（url,params）
"""
import pytest
import requests


class TestDepartment:

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
        #print(r.json()["access_token"])

    @pytest.mark.skip
    def test_create_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params = {
            "access_token": self.token
        }
        json = {
            "name": "西安研发中心",
            "name_en": "RDXA",
            "parentid": 1,
            "order": 1,
            "id": 4
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    @pytest.mark.skip
    def test_update_department(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/department/update"
        params = {
            "access_token": self.token
        }
        json = {
            "name": "西安研发中心2",
            "name_en": "RDXA",
            "parentid": 1,
            "order": 1,
            "id": 4
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errmsg"] == 'updated'

    @pytest.mark.skip
    def test_delete_department(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        params={
            "access_token": self.token,
            "id":2
        }
        r=requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    def test_get_departmentlist(self):
        url="https://qyapi.weixin.qq.com/cgi-bin/department/list"
        params={
            "access_token": self.token,
            "id":3  # 去掉id参数则获取的是所有部门的列表信息，加上id则显示id对应部门的列表信息
        }
        r=requests.get(url=url,params=params)
        print(r.json())
        assert r.json()["errcode"] == 0
