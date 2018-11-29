# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from dbcon import DBConnect
#from pyvirtualdisplay import Display
from search_craw import Search
from datetime import datetime

#display = Display(visible=0, size=(800, 600))
#display.start()

driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)

last_num = 2600

while True:
	driver.get('http://cs.skku.edu/news/recruit/list')

	recent_num = driver.find_element_by_xpath('//*[@id="boardList"]/tbody/tr[2]/td[1]').text
	while True:
		if int(recent_num) > last_num:
			URL = 'http://cs.skku.edu/news/recruit/view/'+str(last_num)
			field = 'IT'
			last_num = last_num+1
			driver.get(URL)

			title = driver.find_element_by_xpath('//*[@id="title"]').text
			print(URL)
			if not title:
				continue
			contents = driver.find_element_by_xpath('//*[@id="text"]').text

			print(title)
			#print(contents)
			db = DBConnect()
			db.make(field, title, contents, URL)
		else:
			break


	sleep(100)