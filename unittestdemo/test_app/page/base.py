# 创建的BasePage类，主要用于封装一些需要重复调用的方法，比如driver
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 在start中定义的driver，使用main函数传递出来，需要在其他所有类中调用，改造到在基类basepage中接收到driver，
    # 并定义driver,然后其他所有类继承基类既可直接调用driver
    def __init__(self, driver: WebDriver = None):
        self.driver = driver