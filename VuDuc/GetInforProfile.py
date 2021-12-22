import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
import requests
import json
import csv

API_URL = 'https://api.gologin.com'

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWMzOGJmZWRkMjVjN2E2ZWExZGI5OTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWMzOGMwYWRkMjVjNzNlMzkxZGI5YTcifQ.LjbBN8Vb3ZdpHkVxcruthJOa1l1UZOo1cVK_4wJ9J3Y"
profile_id= "61c3905de3673d12ca89f33e"
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
a=requests.get(API_URL + '/browser/v2?page=1' , headers=headers)
profile=json.loads(a.content.decode('utf-8'))
print(profile)
with open('Result1.json', 'w') as f:
	json.dump(profile, f)
	print('Done Json')
