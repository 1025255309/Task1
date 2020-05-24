import pytest

def setup_module():
    print("这是setup_module方法")

def teardown_module():
    print("这是teardown_module方法")

def setup_fuction():
    print("这是setup_fuction方法")

def teardown_fuction():
    print("这是teardown_fuction方法")

def test_x():
    print("开始执行test_x 方法")
    x = 'hello'
    assert 'e' in x

# def test_one(self):
#     print("开始执行test_one 方法")
#     x='this'
#     #assert 'h' in x
#     pytest.assume('h' in x)
#     pytest.assume(1==2)
#     pytest.assume(2==2)
#
# def test_two(self):
#     print("开始执行test_two 方法")
#     x = 'hello'
#     assert 'e' in x
#
# def test_three(self):
#     print("开始执行test_three 方法")
#     a = 'hello'
#     b='hello world'
#     # assert 'a' not in b
#     assert 'a' in b

class TestDemo1():
    def setup_class():
        print("这是setup_class方法")

    def setup_method():
        print("这是setup_method方法")

    def setup():
        print("这是setup方法")

    def teardown_class():
        print("这是teardown_class方法")

    def teardown_method():
        print("这是teardown_method方法")

    def teardown():
        print("这是teardown方法")

    def test_a(self):
        print("这是一个外部的方法")

    def test_b(self):
        print("开始执行test_b 方法")
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行test_c 方法")
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main()  # 默认执行该路径下所以以test开头的测试用例
    #pytest.main('-v -x TestDemo1'])两种方式
    #pytest.main(['-v','-s','-k','pytest_setup_teardown.py::TestDemo'])
