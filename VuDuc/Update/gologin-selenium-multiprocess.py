import time
import os
from multiprocessing import Pool
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin

   

def scrap(profile):
	gl = GoLogin({
	        'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs',
	        'profile_id': profile['profile_id'],
	        'port': profile['port'],
		})

	if platform == "linux" or platform == "linux2":
		chrome_driver_path = './chromedriver'
	elif platform == "darwin":
		chrome_driver_path = './mac/chromedriver'
	elif platform == "win32":
		chrome_driver_path = 'chromedriver.exe'

	debugger_address = gl.start()
	chrome_options = Options()
	chrome_options.add_experimental_option("debuggerAddress", debugger_address)
	driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)
	driver.get("http://www.python.org")
	print('ready', profile['profile_id'], driver.title)
	time.sleep(10)
	print('closing', profile['profile_id'])
	driver.close()
	gl.stop()
if __name__ == '__main__':    

	profiles = [
		{'profile_id': '61ab00d4de9fef1804e0fc04', 'port': 3500,'a':100}, 
		]


	with Pool(3) as p:
		p.map(scrap, profiles)


	if platform == "win32":
		os.system('taskkill /im chrome.exe /f')
		os.system('taskkill /im chromedriver.exe /f')
	else:
		os.system('killall -9 chrome')
		os.system('killall -9 chromedriver')
