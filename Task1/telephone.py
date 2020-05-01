class Phone():
    powerkey=1
    volumekey=2
    headphonejack=1
    chargingport=1

    def give_call(self):
        print("没事打个电话聊聊天")
    def send_message(self):
        print("重要易错信息就发短信吧")
    def take_photo(self):
        print("来一起拍个照片留做纪念吧")
    def scan_payment(self):
        print("扫一扫立即支付，随机立减最高10元")
    def play_song(self):
        print("来听听歌放松放松吧")
    def charge(self):
        print("哦哦，电量不足，充会电吧")

mi_phone=Phone()
print(mi_phone.play_song())
print(mi_phone.charge())

