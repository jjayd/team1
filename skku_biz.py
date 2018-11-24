# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.implicitly_wait(3)


driver.get('http://biz.skku.edu/kr/boardList.do?bbsId=BBSMSTR_000000000001&noticeCategory=03')

title = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[1]/ul/li[1]/strong/a')
print(title.text)
title.click()
contents = driver.find_element_by_xpath('//*[@id="container"]/div[3]/div[1]/div[4]')
print(contents.text)

sleep(100)
