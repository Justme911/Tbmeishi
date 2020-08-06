# -*- coding = utf-8 -*-
# @Time :2020/8/6 10:00
# @Author :windows
# @Site :
# @File :spider.py
# @SoftWare :PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

def search():
    browser.get("http://www.taobao.com")
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
    )


