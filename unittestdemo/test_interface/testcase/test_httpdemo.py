import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth

class TestHttpDemo:

    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        # payload相当于载体
        payload = {
            "level": 1,
            "name": "sevenirby"
        }
        r = requests.get('http://httpbin.testing-studio.com/get', params = payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "sevenirby"
        }
        # 注意一定要把param改成data,否则不是表单还是query
        r = requests.post('http://httpbin.testing-studio.com/post', data = payload)
        print(r.text)
        assert r.status_code == 200

    def test_headers(self):
        r = requests.get('http://httpbin.testing-studio.com/get',headers= {"h":"headers demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == "headers demo"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "sevenirby"
        }
        # 注意一定要把param改成data,否则不是表单还是query
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200

    def test_hogwarts_json(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'

    def test_hamcrept(self):

        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        # assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        # print(jsonpath(r.json(), '$..name'))
        # assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'
        # assert_that(前面是目标的真实结果，后面是匹配器+内容)
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('霍格沃兹测试学院公众号'))

    def test_cookie_headers(self):
        url = "http://httpbin.testing-studio.com/cookies"
        header = {
            "Cookie": "hogwarts=school",
            "User_Agent": "banana"
        }
        r = requests.get(url=url,headers=header)
        print(r.request.headers)

    def test_cookie(self):
        url = "http://httpbin.testing-studio.com/cookies"
        header = {
            "User_Agent": "banana"
        }
        cookie_data = {
            "hogwarts": "school",
            "teacher": "AD"
        }
        r = requests.get(url=url,headers=header,cookies=cookie_data)
        print(r.request.headers)

    def test_oauth(self):
        r = requests.get(url="http://httpbin.testing-studio.com/basic-auth/banana/123",
                     auth = HTTPBasicAuth("banana","123"))
        print(r)
        print(r.text)
