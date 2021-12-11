import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin

option={
	"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs",
	"profile_id": "61b305469e8d6b057287f8aa",
	"local": False,
	"credentials_enable_service": False,
	"uploadCookiesToServer":True
	}
gl = GoLogin(option)


if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

debugger_address = gl.start()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", debugger_address)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
driver.get("https://share-w.in/f5huty-42970")
fullname=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[1]/input')
fullname.send_keys('1')
emailaddress=driver.find_element_by_xpath('//*[@id="sw_login_fields"]/div[2]/input')
emailaddress.send_keys('ducdeptrai@gmail.com')
telegram=driver.find_element_by_xpath('//*[@id="sw_text_input_11_1"]')
telegram.send_keys('3')
bep20=driver.find_element_by_xpath('//*[@id="sw_text_input_12_1"]')
bep20.send_keys('4')
time.sleep(10)
print('ok')
driver.find_element_by_xpath('//*[@id="sw_login_button"]').click()

print(input('xong'))
# driver.close()
# gl.commitProfile()
gl.stop()
