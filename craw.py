# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from dbcon import DBConnect
from pyvirtualdisplay import Display
from search_craw import Search
from datetime import datetime

display = Display(visible=0, size=(800, 600))
display.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/home/ubuntu/chromedriver',chrome_options=chrome_options)

#driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.implicitly_wait(3)

last_num = 2801

while True:
	driver.get('http://cs.skku.edu/news/recruit/list')
	recent_num = driver.find_element_by_xpath('//*[@id="boardList"]/tbody/tr[2]/td[1]').text
	while True:
		if int(recent_num) > last_num:
			last_num +=1
			URL = 'http://cs.skku.edu/news/recruit/view/'+str(last_num)
			field = 'IT'
			driver.get(URL)
			sleep(5)
			print(URL)
			title=[]
			title = driver.find_elements_by_xpath('//*[@id="title"]')
			if title[0].text=="":
				print("no title\n")
				continue
			print (title[0].text)
			contents = driver.find_element_by_xpath('//*[@id="text"]').text
			print (contents)

			
			db = DBConnect()
			db.make(field, title[0].text, contents, URL)
		
		else:
			break


	sleep(80000)
