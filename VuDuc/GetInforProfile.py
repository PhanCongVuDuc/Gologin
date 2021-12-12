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
profile_id= "61ab00ac5ed8dd56952f1032"
headers = {
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Selenium-API'
}
# gl = GoLogin({
# 	"token": token,
# 	"profile_id": profile_id,
# 	})
# profile=gl.getProfile()
# print(profile)
a=requests.get(API_URL + '/browser/' + profile_id, headers=headers)
profile=json.loads(a.content.decode('utf-8'))
print(profile)
with open('Result1.json', 'w') as f:
	json.dump(profile, f)
	print('Done Json')
