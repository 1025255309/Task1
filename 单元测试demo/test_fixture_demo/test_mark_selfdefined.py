"""
import pytest
#不带参数的fixture默认参数为scope=function
@pytest.fixture()
def login():
    print("这是个登录方法")
def pytest_configure(config):
    marker_list=["search", "login"]  #标签名集合
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )
"""

import pytest
@pytest.mark.search
def test_search1():
    print("test_search1")
    #raise NameError
    pass

@pytest.mark.search
def test_search2():
    print("test_search2")
    pass
@pytest.mark.search
def test_search3():
    print("test_search3")
    pass

@pytest.mark.login
def test_loginl():
    print("test_login1")
    pass
@ pytest.mark.login
def test_login2():
    print("test_loginz")
    pass

if __name__ == '__main__':
    pytest. main("-v")


# 在Terminal中进入该package目录（D:\proiect\单元测试demo\test_fixture_demo）
# pytest -s test_mark_selfdefined.py  测试用例全部执行，且打印全部print信息（-s）
# pytest -s test_mark_selfdefined.py -m search  只执行标记为search的测试用例(-m search)
# pytest -v test_mark_selfdefined.py -m login  只执行标记为login的测试用例,且打印详细信息(-v)