import pytest

# 我们把登录方法放在同目录下的conftest.py中会有同样的作用
# @pytest.fixture()
# def login():
#     print("这是一个登录方法")

def test_01(login):
    print("这是test_01 需要先登录")
    pass

def test_02():
    print("这是test_02 不需要登录")
    pass

def test_03(login):
    print("这是test_03 需要先登录")
    pass

if __name__ == '__main__':
    pytest.main()
    #pytest.main('-v','-x','test_fixture.py')

# 为啥执行的时候只执行了第二个测试用例？？因为方法1和3需要登陆，忘记传递login这个方法了
