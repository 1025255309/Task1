from selenium.webdriver.common.by import By

from test_po_wechat.pageobject.addmember import AddMember
from test_po_wechat.pageobject.base import Base


class Contact(Base):
    def get_member(self):
        # 得到所有的成员信息
        member_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

        # name_list=[]
        # for member in member_list:
        #     name_list.append(member.get_attribute("title"))
        # return name_list
        # 将上面四行代码做优化写成列表推导式
        return [member.get_attribute("title") for member in member_list]
        # print(name_list)

    def goto_addmember(self):
        return AddMember()

