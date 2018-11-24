# -*- coding: utf-8 -*- 

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import sys, os
import urllib

driver = webdriver.Chrome('/Users/jeongjin-a/Desktop/craw/chromedriver')
driver.implicitly_wait(3)

last_num = 102547


while True:
	cnt=0
	tmp=[]
	driver.get('https://job.skku.edu/login.aspx?redir=/loginproc.aspx%3fredir2%3d%2fdefault.aspx%3f')

	user_id = "jjayd"
	user_pw = "thdhvmxm!16"
	driver.find_element_by_name('user_id').send_keys(user_id)
	driver.find_element_by_name('user_pw').send_keys(user_pw)

	driver.find_element_by_xpath('//*[@id="btnLogin"]').click()

	driver.get("https://job.skku.edu/jobs/all/default.aspx?firstorderby=1&isadregdate=1&page=1")

	
	while True:
		if cnt==10:
			last_num = tmp[0]-1

			print("there is no anymore: "+str(last_num))
			sleep(100)
			break

		# get title

		try:
			driver.get('https://job.skku.edu/jobs/all/view.aspx?jobidx='+str(last_num+1))
			title = driver.find_element_by_xpath('//*[@id="ApplyFrm"]/div/div[3]/h2[1]').text

		except:
			last_num+=1
			print("no files: "+str(last_num))
			tmp.append(last_num)
			cnt+=1	
			driver.switch_to_alert()
			driver.switch_to_alert().accept()
			continue

		if cnt:
			cnt=0
			tmp=[]	


		content=[]
		pcnt=2
	
		last_num=last_num+1
		print("exist file: "+str(last_num))
		print(title)



		# get contents with text

		try:
			while True:
				content.append(driver.find_element_by_xpath('//*[@id="ApplyFrm"]/div/div[3]/p['+str(pcnt)+']').text)
				print(driver.find_element_by_xpath('//*[@id="ApplyFrm"]/div/div[3]/p['+str(pcnt)+']').text)
				pcnt+=1
		except:
			print("fin\n")


		# get contents with images

		for i in range(1,5):
			try:
				img = driver.find_element_by_xpath('//*[@id="ApplyFrm"]/div/div[3]/p['+str(i)+']/img')
				print("trying\n")
				if img:
					print("there is images!!\n")
					src=img.get_attribute('src') #f etch the location of image 
					print("img: "+src)
			except:
				continue

		print("plzzzzzz\n")





		



