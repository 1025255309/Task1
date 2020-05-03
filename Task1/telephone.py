"""
作业2-2：用类和面向对象的思想，“描述”生活中任意接触到的东西-------我的小米手机mi_phone
"""
# 定义一个父类Phone
class Phone():
    # 定义公共属性，静态属性
    powerkey = 1
    volumekey = 2
    headphonejack = 1
    chargingport = 1

    def give_call(self):
        print("没事打个电话聊聊天")

    def send_message(self):
        print("重要易错信息就发短信吧")

# 定义一个子类telephone继承于父类Phone
class Telephone(Phone):
    # 定义一个私有属性，私有变量，可以在类方法中调用,但不能在类外部直接调用
    __cardslot = 2

    def take_photo(self):
        print("来一起拍个照片留做纪念吧")

    def scan_payment(self):
        # 在类方法中可以通过self.直接调用私有变量
        print(self.__cardslot)
        print("扫一扫立即支付，随机立减最高10元")

    def play_song(self):
        print("来听听歌放松放松吧")

    def charge(self):
        print("哦哦，电量不足，充会电吧")

    # 定义一个私有属性，私有方法
    def __play_when_charge(self):
        print("哦哦，电量不足，充会电吧")
        # 在方法中使用self.来调用另一个方法，也就是实现在手机充电的时候听歌
        self.play_song()

mi_phone = Telephone()
print(mi_phone.volumekey)
mi_phone.send_message()
# print(mi_phone.take_photo())
# print(mi_phone.charge())
mi_phone.take_photo()
mi_phone.charge()
# 注意外部无法调用私有变量，mi_phone.__cardslot就会失败，在类方法中调用后可以正确打印
mi_phone.scan_payment()
# 通过name重写的方法可以调用私有属性，注意格式:对象._类名_私有方法名（），相当于指定门牌号,但是不建议这样使用，私有就是不想让人调用的
mi_phone._Telephone__play_when_charge()
