"""
作业2-3：用类和面向对象的思想，“描述”生活中任意接触到的东西-------学生xiaoming和老师lilei
1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
创建方法study参数为Teacher对象，调用Teacher类的teachobj方法，接收老师教授的知识点，然后打印‘老师,xxx我终于学会了！’xxx为老师的teach方法返回的信息。
3、创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。
创建teachobj方法，返回信息为‘今天讲了如何用面向对象设计程序’
4、实例化一个学生xiaoming和一个老师lilei，学生对象调用teach方法
"""


class Person:  # 定义一个Person类
    def __init__(self, name, age, gender):  # 使用构造函数对类进行初始化，同时传3个参数
        self.name = name
        self.age = age
        self.gender = gender

    def personinfo(self):  # 定义打印基本信息的方法
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender}")


class Student(Person):  # 定义Student类，继承于Person
    def __add__(self, college, class1):  # 定义一个私有属性，同时传2个参数，其中为避免班级参数class和系统关键字class重名，特改为class1
        self.college = college
        self.class1 = class1

    def personinfo(self):  # 定义打印基本信息的方法
        print(
            f"name: {self.name}, age: {self.age}, gender: {self.gender}, college: {self.college},class1: {self.class1}")

    def study(self, teach1):  # 定义学习的方法，并传入一个参数,此处为与后面老师方法teach方法重名，改为teach1
        self.teach1 = teach1
        print("老师,{}我终于学会了".format(teach1))


class Teacher(Person):  # 定义Teacher类，继承于Person
    def __init__(self, name, age, gender, college, professional):  # 重新构造函数并对类初始化，同时传入5个参数
        super().__init__(name, age, gender)  # 通过super调用Person类的构造函数传入前三个参数
        self.college = college
        self.professional = professional

    def personinfo(self):  # 定义打印基本信息的方法
        print(
            f"name: {self.name}, age: {self.age}, gender: {self.gender}, college: {self.college},professional: {self.professional}")

    def teacherobj(self):  # 定义授课内容的方法
        print("今天讲了如何用面向对象设计程序")

    def teach(self):  # 定义课程类型的方法
        print("python面向对象")
        return "python面向对象"


xiaoming = Student("xiaoming", 18, "female")  # 实例化一个学生xiaoming，同时传入3个参数
xiaoming.__add__("北京大学", "202005")  # 调用私有函数传入2个参数
xiaoming.personinfo()  # 此处注意，打印的信息有5个参数，包括实例化类传入的3个和调用私有属性传入的2个

lilei = Teacher("lilei", 30, "male", "北京大学", "python")  # 实例化一个老师lilei,同时传入5个参数，这种方法和学生分两次传5个参数都可以，这个更方便
lilei.personinfo()  # 实例化对象调用打印基本信息的方法
lilei.teacherobj()  # 实例化对象调用授课内容的方法
xiaoming.study(lilei.teach())  # Student实例化对象调用学习的方法，同时通过调用Teacher的实例化对象调用课程类型的结果作为参数传入
