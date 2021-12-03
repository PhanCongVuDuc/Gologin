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

headers = {
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Selenium-API'
}


a=requests.get(API_URL + '/browser/' , headers=headers)
b=json.loads(a.content.decode('utf-8'))
print(type(b))
with open('Result1.json', 'w') as f:
	json.dump(b, f)
	print('Done Json')