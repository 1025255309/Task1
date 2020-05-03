"""
作业2-5：用类和面向对象的思想，“描述”生活中任意接触到的东西-------我的电动自行车myebicycle
"""
class Bicycle:
    wheel=2
    handlebar=2
    speaker=1

    def run(self,km):
        self.km=km
        print("人力骑行里程数为{}".format(km))

class Ebicycle(Bicycle):
    def get_charge(self):
        print("电量不足，请及时充电")
    def emax_run(self,ekm):
        print("电瓶支持的最大骑行里程为{}".format(ekm))
    def type_run(self,totalkm,ekm):
        self.totalkm=totalkm
        self.ekm=ekm
        km=totalkm-ekm
        if totalkm <= ekm:
            print("电瓶支持骑行里程数为{}".format(totalkm))
        else:
            print("电瓶支持骑行里程数为{}".format(ekm))
            # print("人力骑行里程数为{}".format(km))
            # 此处括号中的必须传一个参数，为了不覆盖传入的totalkm,ekm
            super().run(km)

my_ebicycle=Ebicycle()
# my_ebicycle.run(100)
# my_ebicycle.emax_run()
my_ebicycle.type_run(110,100)



