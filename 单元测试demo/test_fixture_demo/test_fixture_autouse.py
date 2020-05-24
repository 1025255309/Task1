import pytest

@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")
    yield

    print("执行teardown！")
    print("最后关闭浏览器")

def test_search1():
    print("test_search1")
    pass

def test_search2():
    print("test_search2")
    pass

def test_search3():
    print("test_search3")
    pass

if __name__ == '__main__':
    pytest.main()