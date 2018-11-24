# -*- coding: utf-8 -*- 
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/Users/jeongjin-a/Desktop/craw/chromedriver')
driver.implicitly_wait(3)

last_num = 813


while True:
	driver.get('http://job.postech.ac.kr/index.php/sample-page/?pageid=1&mod=list&category1=%EC%B1%84%EC%9A%A9%EA%B3%B5%EA%B3%A0')

	recent_num = driver.find_element_by_xpath('//*[@id="kboard-default-list"]/div[4]/table/tbody/tr[1]/td[1]').text

	while True:
		if int(recent_num) > last_num:

			driver.get('http://job.postech.ac.kr/index.php/sample-page/?pageid=1&mod=list&category1=%EC%B1%84%EC%9A%A9%EA%B3%B5%EA%B3%A0')
			
			driver.find_element_by_xpath('//*[@id="kboard-default-list"]/div[4]/table/tbody/tr['+str(int(recent_num)-last_num)+']/td[2]/a/div').click()

			last_num=last_num+1
			
			title = driver.find_element_by_xpath('//*[@id="kboard-default-document"]/div[1]/div[1]/h1').text
			contents = driver.find_element_by_xpath('//*[@id="kboard-default-document"]/div[1]/div[3]/div').text
			
			print(title)
			print(contents)


			try:
				img = driver.find_element_by_xpath('//*[@id="kboard-default-document"]/div[1]/div[3]/div/img').get_attribute('src')
	
				print("img: "+img)

			except:
				print("")


			try:
				url = driver.find_element_by_xpath('//*[@id="kboard-default-document"]/div[1]/div[5]/button').get_attribute('onclick')
	
				print("url: "+url[22:-1])

			except:
				print("")

		else:
			break

	sleep(100)




