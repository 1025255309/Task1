"""
安装PO模式编写测试用例的思路：
1.根据界面封装po类与方法，实现暂时设置为空
2.编写用例
3.实现po内的方法，与自动化框架开始结合
4.调试
"""

from test_po_demo.page.indexpage import IndexPage

class TestRegister():
    def test_register(self):
        index = IndexPage()
        # 1.点击登录进入登录页面，
        # 2.点击立即注册，进入注册页面，
        # 3.开始注册
        index.goto_login().goto_register().register()
        # index.goto_register().register()