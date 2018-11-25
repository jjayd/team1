# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from dbcon import DBConnect
from pyvirtualdisplay import Display
from search_craw import Search
from datetime import datetime

display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.implicitly_wait(3)

last_num = 2774
db = DBConnect()

while True:
	driver.get('http://cs.skku.edu/news/recruit/list')

	recent_num = driver.find_element_by_xpath('//*[@id="boardList"]/tbody/tr[2]/td[1]').text
	if int(recent_num) > last_num:
		URL = 'http://cs.skku.edu/news/recruit/view/'+str(recent_num)
		driver.get(URL)
		title = driver.find_element_by_xpath('//*[@id="title"]').text
		contents = driver.find_element_by_xpath('//*[@id="text"]').text

		print(title)
		print(contents)
		field = "CS"
		sc = Search
		(num1, num2, num3, num4) = sc.period(contents)
		year = datetime.today().year
		FinishDate = str(year)+"-"+str(num3) +"-" +str(num4)
		cate = sc.category(title)
		if cate == "취업" :
			category = 1
		elif cate == "인턴" :
			category = 2
		else :
			category = 3
		PostDate = str(datetime.today().year) + "-" + str(datetime.today().month) + "-" + str(datetime.today().day)
		FinishDate = str(year) + "-" + str(num3) + "-" + str(num4)
		if category != 3 :
			db.insert(title, contents, category, field, FinishDate, URL, PostDate)




	sleep(100)