from selenium import webdriver
from selenium.webdriver.common.by import By

from test_po_wechat.pageobject.addmember import AddMember
from test_po_wechat.pageobject.base import Base
from test_po_wechat.pageobject.contact import Contact


class Main(Base):

    def goto_addmember(self):
        # 点击跳转到添加成员页面
        self.driver.find_element(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
        return AddMember()

    def goto_contact(self):
        # 点击跳转通讯录页面
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']/span").click()
        return Contact()