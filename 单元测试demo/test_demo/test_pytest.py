import pytest


def test_x(self):
    print("开始执行test_two 方法")
    x = 'hello'
    assert 'e' in x

class TestDemo():
    def test_one(self):
        print("开始执行test_one 方法")
        x='this'
        #assert 'h' in x
        pytest.assume('h' in x)
        pytest.assume(1==2)
        pytest.assume(2==2)

    def test_two(self):
        print("开始执行test_two 方法")
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print("开始执行test_three 方法")
        a = 'hello'
        b='hello world'
        # assert 'a' not in b
        assert 'a' in b

class TestDemo1():
    def test_a(self):
        print("开始执行test_a 方法")
        x='this'
        assert 'h' in x

    def test_b(self):
        print("开始执行test_b 方法")
        x = 'hello'
        assert 'e' in x

    def test_c(self):
        print("开始执行test_c 方法")
        a = 'hello'
        b='hello world'
        assert 'a' not in b

if __name__ == '__main__':
    #pytest.main()  # 默认执行该路径下所以以test开头的测试用例
    #pytest.main('-v -x TestDemo1'])两种方式
    pytest.main(['-v','-x','TestDemo1'])