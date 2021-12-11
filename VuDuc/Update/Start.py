import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import infor
from selenium.webdriver.common.by import By

links=['https://share-w.in/f5huty-42970','https://share-w.in/3f8n19-42969']


start=input('start: ')
# end=input('end: ')  
print(str(start))

for x in range(int(start)-1,int(start)):
	index=x
	try:
		profile_id=infor.sheet.cell_value(index, 9)
		gmail=infor.sheet.cell_value(index, 11)
		name=infor.sheet.cell_value(index, 12)
		telegramtext=infor.sheet.cell_value(index, 13)
		addresstext=infor.sheet.cell_value(index, 14)

		option={
			"token": infor.token,
			"profile_id": profile_id,
			"local": False,
			"credentials_enable_service": False,
			}
		gl = GoLogin(option)

		if platform == "linux" or platform == "linux2":
			chrome_driver_path = "./chromedriver"
		elif platform == "darwin":
			chrome_driver_path = "./mac/chromedriver"
		elif platform == "win32":
			chrome_driver_path = "chromedriver.exe"

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
			fullname=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[1]/input')
			fullname.clear()
			fullname.send_keys(name)
			emailaddress=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[2]/input')
			emailaddress.clear()
			emailaddress.send_keys(gmail)
			telegram=driver.find_element_by_xpath('//*[@id="sw_text_input_11_1"]')
			telegram.clear()
			telegram.send_keys(telegramtext)
			bep20=driver.find_element_by_xpath('//*[@id="sw_text_input_12_1"]')
			bep20.clear()
			bep20.send_keys(addresstext)
		# for x in range(len(links)):
		# 	driver.switch_to.window(driver.window_handles[0])
		# 	linktext="window.open('{}')".format(links[x])
		# 	driver.execute_script(linktext)
		# 	# driver.get("https://share-w.in/f5huty-42970")
		# 	driver.switch_to.window(driver.window_handles[x+1])
		# 	fullname=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[1]/input')
		# 	fullname.clear()
		# 	fullname.send_keys(name)
		# 	emailaddress=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[2]/input')
		# 	emailaddress.clear()
		# 	emailaddress.send_keys(gmail)
		# 	telegram=driver.find_element_by_xpath('//*[@id="sw_text_input_11_1"]')
		# 	telegram.clear()
		# 	telegram.send_keys(telegramtext)
		# 	bep20=driver.find_element_by_xpath('//*[@id="sw_text_input_12_1"]')
		# 	bep20.clear()
		# 	bep20.send_keys(addresstext)
		# 	# time.sleep(10)
		# 	# print('ok')
		# 	# driver.find_element_by_xpath('//*[@id="sw_login_button"]').click()

		# driver.close()
		# time.sleep(3)
		# gl.stop()
		print(index+1)
	except:
		print(str(index+1)+" An exception occurred")