# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.implicitly_wait(1)


driver.get('https://job.skku.edu/login.aspx?redir2=/')
driver.find_element_by_name('user_id').send_keys('') #아이디 입력
driver.find_element_by_name('user_pw').send_keys('') #비밀번호 입력
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
driver.find_element_by_xpath('//*[@id="gnbtopmenu1"]/a').click()
driver.find_element_by_xpath('//*[@id="leftmenu_leftmenu"]/ul[1]/li[7]/a').click()

for i in range(1, 26):
    title = driver.find_element_by_xpath('//*[@id="contents"]/table/tbody/tr['+str(i)+']/td[3]/a')
    print(title.text)
    title.click()
    contents = driver.find_element_by_xpath('//*[@id="ApplyFrm"]/div/div[3]')
    print(contents.text)
    driver.back()



