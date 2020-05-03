"""
作业2-1：用类和面向对象的思想，“描述”生活中任意接触到的东西-------我老公my_husband和我儿子my_son
"""
# 定义一个人类Person
class Person:
    # 属性，类变量，也叫静态变量
    head = 1
    hand = 2
    arm = 2
    leg = 2
    ear = 2
    eye = 2
    nose = 1
    mouth = 1

    # 定义一个公共属性
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def speak(self):
        print("没事唠唠嗑")
    def eat(self):
        print("民以食为天，先解决温饱问题")

# 定义一个男人的类，继承于人类Person
class Man(Person):
    def work(self):
        print("努力工作，养家糊口")
    def eat(self):
        # 由于父类中也有eat这个方法，想调用父类中的eat方法，需要用到super()
        super().eat()
        print("吃饱才有力气干活")
    # 定义一个私有属性
    def __att_set(self, value):
        self.value = value
        return
# 定义一个儿子的类Son，继承于Man
class Son(Man):
    # 定义在类中的函数，也叫类方法，对应于静态变量，也叫动态属性
    def eat(self):
        # 再次使用super()实现父类中的eat方法
        super(Son, self).eat()
        print("妈妈，我饿了，我要吃饭饭")

    def play(self):
        print("妈妈，我想出去玩会")

    def sleep(self):
        print("妈妈，我好困，我要睡觉觉了")

    def dance(self):
        # print("妈妈，来点misic,我要跳舞啦")
        # 使用f定义输出格式的两种方式
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender} 妈妈，来点misic,我要跳舞啦")
        print(f"name={self.name}, age={self.age}, gender= {self.gender} 妈妈，来点misic,我要跳舞啦")

# 直接调用类的属性和方法
print(Person.eye)
print(Person.eat)
# 给男人类实例化一个对象
my_husband = Man("Jerry",32,"male")
# 调用实例对象中的属性
my_husband.eat()
# 实例化另一个对象
xiaoguoguo = Son("小果果", 1, "male")
# 注意此处的执行结果，使用super()可以调用多层继承关系中相同属性的内容
xiaoguoguo.eat()
# 调用实例化的方法
xiaoguoguo.dance()
# 调用私有属性并打印出来，需要指明类名方能调用，类似指定门牌号
xiaoguoguo._Man__att_set("I am a little fit")
