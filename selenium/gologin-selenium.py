import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
import requests
import json
import csv

API_URL = 'https://api.gologin.com'

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs"
profile_id= "61a7a06989747616f5b8e6ab"

headers = {
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Selenium-API'
}
# a=requests.get(API_URL + '/browser/' , headers=headers)
# b=json.loads(a.content.decode('utf-8'))


# with open('Result.json', 'w') as f:
# 	json.dump(b, f)
# 	print('Done Json')

# keys=b[0].keys()
# with open('Result.csv', 'w', newline='') as f:
# 	dict_writer = csv.DictWriter(f, keys)
# 	dict_writer.writeheader()
# 	dict_writer.writerows(b)
# print('Done CSV')

options={
	"token": token,
	}

gl = GoLogin(options)
gl.create(options)

# gl = GoLogin({
# 	"token": token,
# 	"profile_id": profile_id,
# 	})


# if platform == "linux" or platform == "linux2":
# 	chrome_driver_path = "./chromedriver"
# elif platform == "darwin":
# 	chrome_driver_path = "./mac/chromedriver"
# elif platform == "win32":
# 	chrome_driver_path = "chromedriver.exe"

# debugger_address = gl.start()
# chrome_options = Options()
# chrome_options.add_experimental_option("debuggerAddress", debugger_address)
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# driver.close()
# time.sleep(3)
# gl.stop()
