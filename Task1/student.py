"""
作业2-3：用类和面向对象的思想，“描述”生活中任意接触到的东西-------学生xiaoming和老师lilei
1、创建Person类，属性有姓名、年龄、性别，创建方法personInfo,打印这个人的信息
2、创建Student类，继承Person类，属性有学院college，班级class，重写父类personInfo方法，调用父类方法打印个人信息外，将学生的学院、班级信息也打印出来，
创建方法study参数为Teacher对象，调用Teacher类的teachobj方法，接收老师教授的知识点，然后打印‘老师,xxx我终于学会了！’xxx为老师的teach方法返回的信息。
3、创建Teacher类，继承Person类，属性有学院college，专业professional，重写父类personInfo方法，调用父类方法打印个人信息外，将老师的学院、专业信息也打印出来。
创建teachobj方法，返回信息为‘今天讲了如何用面向对象设计程序’
4、创建一个学生对象xiaoming，分别打印其详细信息
5、创建一个老师对象lilei，打印其详细信息
6、学生对象调用teach方法
————————————————
题目参考原文链接：https://blog.csdn.net/cc576795555/java/article/details/84203126
"""
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def personinfo(self):
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender}")
class Student(Person):
    def __add__(self, college,class1):
        self.college=college
        self.class1=class1

    def personinfo(self):
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender}, college: {self.college},class1: {self.class1}")
    def study(self,teach1):
        self.teach1=teach1
        print("老师,{}我终于学会了".format(teach1))

class Teacher(Person):
    def __init__(self, name, age, gender, college, professional):
        super().__init__(name,age,gender)
        self.college=college
        self.professional=professional
    def personinfo(self):
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender}, college: {self.college},professional: {self.professional}")
    def teacherobj(self):
        print("今天讲了如何用面向对象设计程序")
    def teach(self):
        print("python面向对象")
        return "python面向对象"
xiaoming=Student("xiaoming",18,"female")
xiaoming.__add__("北京大学","202005")
xiaoming.personinfo()

lilei=Teacher("lilei",30,"male","北京大学","python")
lilei.personinfo()
lilei.teacherobj()
xiaoming.study(lilei.teach())

