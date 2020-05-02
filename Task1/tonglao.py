# 定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
# see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
# fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
# 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
# 加入模块化改造

class TongLao:  # 定义童姥类
    def __init__(self, hp, power):  # 定义构造函数，带有两个参数血量hp和武力值power
        self.hp = hp
        self.power = power

    def see_people(self, name):  # 定义类方法see_people，根据不同人，打印不同内容
        self.name = name
        if self.name == "无崖子":
            print("师弟！！！！")
        elif self.name == "李秋水":
            print("呸，贱人")
        elif self.name == "丁春秋":
            print("叛徒！我要杀了你")

    def __run(self):  # 定义私有方法（__方法名），制定私有逃跑计划
        print("三十六计走为上计")

    def fight_zms(self, enemy_hp, enemy_power):  # 定义一个天山折梅手fight_zms方法，并传参
        final_hp = self.hp / 2 - enemy_power
        final_enemy_hp = enemy_hp - self.power * 10
        if (final_hp > final_enemy_hp):  # if语句实现一回合制对打，打完之后，比较双方血量，血多的一方获胜
            print("还不快滚，下次别让我再见到你！")
        elif (final_hp == final_enemy_hp):
            print("没想到你小子还真有两下子")
        else:
            print("今天状态不好，竟然输给这个臭小子")
            self.__run()

class XuZhu(TongLao):  # 定义虚竹类，继承于天山童姥类
    def read(self):  # 定义一个念经的方法
        print("罪过罪过")

tianshantonglao = TongLao(1000, 10)  # 实例化一个天山童姥，并传参血量和武力值
tianshantonglao.see_people("丁春秋")  # 调用实例化see_people方法，并传参
tianshantonglao.fight_zms(1000, 100)  # 调用实例化fight_zms方法，并传参
xuzhu = XuZhu  # 将虚竹类赋给变量xuzhu
print(xuzhu.read)  # 直接调用类read方法
x = XuZhu(500, 10)  # 实例化一个虚竹类为对象x
x.read()  # 调用实例化对象x的read方法
