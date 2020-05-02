class Person:
    # 属性，类变量，也叫静态变量
    head = 1
    hand = 2
    arm = 2
    leg = 2
    ear = 2
    eye = 2
    nose = 1
    mouse = 1

    # 定义一个公共属性
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 再定义一个私有属性
    def att_set(self, value):
        self.value = value
        return value

    # 定义在类中的函数，也叫类方法，对应于静态变量，也叫动态属性
    def eat(self):
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
# 实例化一个对象
my_son = Person
# 调用实例对象中的属性
print(my_son.eat)
# 实例化另一个对象
xiaoguoguo = Person("小果果", 1, "male")
# 调用实例化的方法
xiaoguoguo.dance()
# 调用私有属性并打印出来
print(xiaoguoguo.att_set("I am a little fit"))
