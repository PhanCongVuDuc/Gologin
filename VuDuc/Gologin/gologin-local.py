import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs'
profile_id='61ab00b06cf85c35879f3368'
option={
	"token": token,
	"profile_id": profile_id,
	"local": False,
	"credentials_enable_service": False,
	}
link=['https://share-w.in/f5huty-42970','https://share-w.in/3f8n19-42969']
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
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=chrome_options)
driver.execute_script("window.open('https://www.yahoo.com')")
driver.execute_script("window.open('https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python')")





assert "Python" in driver.title

driver.close()
time.sleep(3)
gl.stop()
