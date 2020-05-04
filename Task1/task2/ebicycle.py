"""
作业2-5：用类和面向对象的思想，“描述”生活中任意接触到的东西-------我的电动自行车myebicycle
1.定义一个Bicycle类，有静态属性车轮，车把手，车喇叭，有动态方法run，并打印骑行里程数
2.定义一个Ebicycle类，继承于Bicycle，定义充电方法，电瓶支持的最大骑行里程方法，骑行类型方法，加入判断，
  总里程数超过电瓶支持的最大里程数之后就需要调用父类run方法
"""


class Bicycle:  # 定义一个Bicycle类
    wheel = 2
    handlebar = 2
    speaker = 1

    def run(self, km):  # 定义一个骑行的方法，同时传入一个参数km
        self.km = km
        print("骑行总里程数为{}".format(km))


class Ebicycle(Bicycle):  # 定义一个Ebicycle类，继承于Bicycle类
    def get_charge(self):
        print("电量不足，请及时充电")

    def emax_run(self, ekm):  # 定义一个电动最大骑行的方法，同时传入一个参数ekm
        self.ekm = ekm  # 初始化一个值
        print("电瓶支持的最大骑行里程为{}".format(ekm))

    def type_run(self):  # 定义一个骑行类型的方法
        # super().run()
        # self.emax_run()
        skm = self.km - self.ekm  # 定义一个变量skm，并将总里程数与电瓶骑行最大里程数的插值赋给skm
        if skm <= 0:  # 使用if语句判断，如果ekm为负值，则骑行里程为电瓶支持骑行里程数，反之，电瓶支持骑行最大里程数，且skm为人力骑行里程数
            print("电瓶支持骑行里程数为{}".format(self.km))
        else:
            print("电瓶支持骑行里程数为{}".format(self.ekm))
            print("人力骑行里程数为{}".format(skm))


my_ebicycle = Ebicycle()  # 实例化对象my_ebicycle
my_ebicycle.run(110)  # 实例化对象调用父类run的方法，并传递一个参数
my_ebicycle.emax_run(100)  # 实例化对象调用emax_run的方法，并传递一个参数
my_ebicycle.type_run()  # 实例化对象调用type_run的方法
