from selenium.webdriver.common.by import By

from test_po_wechat.pageobject.contact import Contact
from test_po_wechat.pageobject.base import Base

class AddMember(Base):
    def addmember(self):
        # 姓名
        self.driver.find_element(By.ID,"username").send_keys("阿华")
        # 账号
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("8945612")
        # 手机
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys("13811111111")
        # 保存
        self.driver.find_element(By.XPATH, "//*[@id='js_contacts125']/div/div[2]/div/div[4]/div/form/div[3]/a[2]")
        return Contact()


