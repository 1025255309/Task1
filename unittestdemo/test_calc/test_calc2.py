# 主要为了演示@pytest.mark.parametrize()传入方法的高级用法，也就是录播疑问https://home.testing-studio.com/t/topic/2116/2
# 导入pytest
import pytest
# 导入Calc
import yaml

from python_code.calc import Calc
from decimal import Decimal
import yaml

from decimal import Decimal

# 定义一个列表
datas = (
    (1, 2, 3),
    (100, 200, 300),
    [0, 9, 9]
)

# 定义一个fixture,哪个方法需要使用就传给哪个方法
@pytest.fixture()
# 定义一个方法
def get_data(request):  # request是fixture的一个参数，传入一个request，可以给它一个列表，但必须是以request.para接收的
    return request.param


# 定义一个计算机的测试用例类
class TestCalc:
    # 使用@pytest.mark.parametrize()高级用法传入一个方法，如果是以参数的形式传入方法的话parametrize有个规则，就是需要加上indirect=True
    @pytest.mark.parametrize('get_data',datas,indirect=True)
    # 定义一个加的测试用例
    def test_add(self,get_data):
        print((f"get_data={get_data}"))  # 方法名就代表它return回来的数据
        result = self.calc.add(get_data[0], get_data[1])
        print(f'result={result}')
        assert result == get_data[2]


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
