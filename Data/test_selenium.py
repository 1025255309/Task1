import selenium
from selenium import webdriver

def __init__():

def go_baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.find_element_by_id("").send_keys("")