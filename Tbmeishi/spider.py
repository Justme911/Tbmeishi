# -*- coding = utf-8 -*-
# @Time :2020/8/6 10:00
# @Author :windows
# @Site :
# @File :spider.py
# @SoftWare :PyCharm
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()


options = webdriver.ChromeOptions()
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])
self.browser = webdriver.Chrome( options=options)
wait = WebDriverWait(self.browser , 10)
def search():
    self.browser.get("http://www.taobao.com")
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#q")))
    submit = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button")))
    input.send_keys('美食')
    submit.click()


def main():
    search()

if __name__ == '__main__':
    main()