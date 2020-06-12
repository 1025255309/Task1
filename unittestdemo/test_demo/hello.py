"""
类变量 实例变量区别
类方法，实例方法区别
"""
# 定义一个类
class Hello:
    # 类中的方法必须带默认参数self，self代表类的实例，只有实例化后的对象可以调用类的方法，装饰器中也无法调用self
    def a1(self):
        print("a1")
    # 如果类Hello想调用类方法，需要在类方法前面加装饰器@classmethod
    @classmethod
    def a2(self):
        print("a2")

h=Hello()  # 实例化一个对象
h.a1()  # 这是实例化的对象，就可以直接调用类方法，
h.a2()
# print(Hello.a1())  # 直接报错，因为类不能直接调用类方法
Hello.a2()  # 在类方法a2前面加装饰器@classmethod,所以可以直接调用