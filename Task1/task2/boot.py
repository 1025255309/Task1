"""
作业2-4：用类和面向对象的思想，“描述”生活中任意接触到的东西-------行李箱myboot
1.设计一个立方体类Box，定义三个属性，分别是长，宽，高。定义二个方法，分别计算并输出立方体的体积和表面积。
2.设计一个行李箱类Boot,继承于Box,调用父类两个方法，计算出容积（体积）和表面积，定义一个方法获取重量，同时传递一个重量参数；
再定义一个坐飞机的方法，并预定体积大小超过20*40*55(=44000立方厘米)或重量大于10千克则无法带上飞行，需要托运
"""


class Box:  # 定义一个Box类
    def __init__(self, width, height, depth):  # 使用构造函数对类进行初始化，同时传3个参数
        self.width = width
        self.height = height
        self.depth = depth

    def get_volume(self):  # 定义一个获取体积的方法
        volume = self.width * self.height * self.depth
        print("体积是{}立方厘米".format(volume))

    def get_area(self, ):  # 定义一个获取面积的方法
        area = (self.width + self.height + self.depth) * 2
        print("表面积是{}平方厘米".format(area))


class Boot(Box):  # 定义一个Boot类，继承于Box类
    def get_weight(self, kg):  # 定义一个获取重量的方法，同时传入一个参数
        self.kg = kg
        print("箱子体重是{}千克".format(kg))

    def by_airplane(self):  # 定义一个坐飞机的方法
        volume = self.width * self.height * self.depth  # 注意父类中的变量无法直接调用，需要重新定义赋值
        if (volume > 44000 or self.kg > 10 or self.width > 20 or self.height > 40 or self.depth > 55):
            print("箱子超重，请办理托运")
        else:
            print("箱子可随身携带上飞机")


my_boot = Boot(22, 40, 50)  # 实例化一个对象my_boot,同时传入3个参数
my_boot.get_volume()  # 实例化对象调用获取体积的方法
my_boot.get_area()  # 实例化对象调用获取面积的方法
my_boot.get_weight(8)  # 实例化对象调用获取重量的方法，并传入8，也就是8千克
my_boot.by_airplane()  # 实例化对象调用坐飞机的方法
