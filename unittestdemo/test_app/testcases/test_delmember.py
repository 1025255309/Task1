"""
作业：删除员工
打开企业微信-进入首页---定位通讯录并点击-进入通信录页面---定位右上角编辑并点击-进入管理通讯录页面
---定位要删除的员工行并点击-进入编辑页面---定位删除员工并点击-进入确认删除弹框---定位确认并点击即可删除
断言：删除完成后跳转回管理通讯录页面
"""
from test_app.page.workweixin import App


class TestContact:
    def setup(self):
        self.app = App()

    def teardown(self):
        pass

    def test_delmember(self):
        self.app.start().main().goto_contact()

