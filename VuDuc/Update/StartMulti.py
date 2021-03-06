import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import information
from selenium.webdriver.common.by import By
import os
from multiprocessing import Pool

links=['https://sweepwidget.com/view/43260-yinp7cmo/oib8y1-43260']

def scrap(profile):
	index=profile['index']
	try:
		profile_id=profile['profile_id']
		gmail=information.sheet.cell_value(index, 11)
		name=information.sheet.cell_value(index, 12)
		telegramtext=information.sheet.cell_value(index, 13)
		addresstext=information.sheet.cell_value(index, 14)

		option={
			"token": information.token,
			"profile_id": profile_id,
			"local": False,
	        'port': profile['port'],
			}
		gl = GoLogin(option)

		debugger_address = gl.start()
		print(debugger_address)
		chrome_options = Options()
		chrome_options.add_experimental_option("debuggerAddress", debugger_address)
		driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)

		for link in links:
			driver.switch_to.window(driver.window_handles[0])
			linktext="window.open('{}')".format(link)
			driver.execute_script(linktext)


		for x in range(len(links)):
			driver.switch_to.window(driver.window_handles[x+1])
			time.sleep(1)
			fullname=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[1]/input')
			fullname.clear()
			fullname.send_keys(name)
			emailaddress=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[2]/input')
			emailaddress.clear()
			emailaddress.send_keys(gmail)
			# telegram=driver.find_element_by_xpath('//*[@id="sw_text_input_11_1"]')
			# telegram.clear()
			# telegram.send_keys(telegramtext)
			bep20=driver.find_element_by_xpath('//*[@id="sw_text_input_17_1"]')
			bep20.clear()
			bep20.send_keys(addresstext)

			time.sleep(3)
			driver.find_element_by_xpath('//*[@id="sw_login_button"]').click()
		print(str(index+1)+'done')

	except:
		print(str(index+1)+" An exception occurred")

	time.sleep(2)
	driver.close()
	driver.switch_to.window(driver.window_handles[0])
	driver.close()

	print(str(index+1)+'close')

if __name__ == '__main__':

	start=input('start: ')
	end=input('end: ')  
	print(str(start)+"-->"+str(end))

	profiles = []
	port1=3500
	for x in range(int(start)-1,int(end)):
		index=x
		error=information.sheet.cell_value(index, 0)
		if error!=31 and error!=1:
			try:
				profile_id=information.sheet.cell_value(index, 9)
				information=dict()
				information['profile_id']=profile_id
				information['index']=index
				information['port']=port1
				profiles.append(information)

				port1=port1+1
				print('Add: '+str(index+1))
			except:
				print(str(index+1)+"- An exception occurred")
	with Pool(15) as p:
		p.map(scrap, profiles)

