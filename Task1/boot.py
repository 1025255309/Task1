"""
作业2-4：用类和面向对象的思想，“描述”生活中任意接触到的东西-------行李箱myboot
1.设计一个立方体类Box，定义三个属性，分别是长，宽，高。定义二个方法，分别计算并输出立方体的体积和表面积。
2.设计一个行李箱类Boot,继承于Box,调用父类两个方法，计算出容积（体积）和表面积，定义一个方法获取重量，同时传递一个重量参数；
再定义一个坐飞机的方法，并预定体积大小超过20*40*55(=44000立方厘米)或重量大于10千克则无法带上飞行，需要托运
"""
class Box:
    def __init__(self,width,height,depth):
        self.width=width
        self.height=height
        self.depth=depth
    def get_volume(self):
        volume=self.width*self.height*self.depth
        print("体积是{}立方厘米".format(volume))
    def get_area(self,):
        area=(self.width + self.height + self.depth)*2
        print("表面积是{}平方厘米".format(area))

class Boot(Box):
    def get_weight(self,kg):
        self.kg=kg
        print("箱子体重是{}千克".format(kg))
    def by_airplane(self):
        # 注意，volume是父类方法中的参数，如果想使用必须重新定义，无法直接引用
        volume = self.width * self.height * self.depth
        if (volume > 44000 or self.kg > 10 or self.width > 20 or self.height > 40 or self.depth > 55):
            print("箱子超重，请办理托运")
        else:
            print("箱子可随身携带上飞机")

my_boot=Boot(22,40,50)
my_boot.get_volume()
my_boot.get_area()
my_boot.get_weight(8)
my_boot.by_airplane()



