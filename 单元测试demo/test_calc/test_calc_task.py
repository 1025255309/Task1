# 导入pytest
import pytest
# 导入Calc
import yaml

from python_code.calc import Calc
from decimal import Decimal
import yaml

from decimal import Decimal

# 定义一个计算机的测试用例类
class TestCalc:
    def setup_class(self):
        print("setup_class")
        self.calc = Calc()

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    # 参数化数据方式传参，可以是列表形式或者元组形式
    # @pytest.mark.parametrize("a,b,expect",[
    #     (1, 1, 2),
    #     [100, 100, 200],
    #     [0.1, 0.1, 0.2],
    #     (0, 10, 10),
    # ])
    # 使用yaml传参，基于数据的数据驱动
    @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("data.yaml")))
    # 定义一个加的测试用例
    def test_add(self,a,b,expect):
        # 实例化一个类
        calc = Calc()
        result = self.calc.add(Decimal(str(a)),Decimal(str(b)))
        print(f'result={result}')
        assert result == Decimal(str(expect))

    # # 使用yaml传参，基于数据的数据驱动
    # @pytest.mark.parametrize("a,b,expect",yaml.safe_load(open("data.yaml")))
    # # 定义一个加的测试用例
    # def test_add(self,a,b,expect):
    #     # 实例化一个类
    #     result = self.calc.add(a, b)
    #     assert result == expect

    # 再定义一个加的测试用例
    # def test_add(self):
    #     # 实例化一个类
    #     calc = Calc()
    #     result = calc.add(0.1, 0.1)
    #     assert result == 0.2

    def test_div(self):
        calc = Calc()
        result = calc.div(1, 1)
        assert result == 1

    def test_yaml(self):
        print(yaml.safe_load(open("data.yaml")))


    # 定义一个除的方法
    def test_div(self):
        pass

if __name__ == '__main__':
    pytest.main(['-vs','test_calc.py'])
