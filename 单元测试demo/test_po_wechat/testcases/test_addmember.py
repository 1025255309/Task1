from test_po_wechat.pageobject.main import Main


class TestAddmember:

    def test_addmember(self):
        main=Main()
        assert "阿华" in main.goto_addmember().addmember().get_member()