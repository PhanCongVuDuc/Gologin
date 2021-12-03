import time
from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
import requests
import json
import csv

API_URL = 'https://api.gologin.com'

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs"
profile_id= "61a8ee1a656d196bcf36d18d"

headers = {
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Selenium-API'
}
options={
  "token": token,
}


def getRandomFingerprint(options):
  os_type = options.get('os', 'lin')
  return json.loads(requests.get(API_URL + '/browser/fingerprint?os=' + os_type, headers=headers).content.decode('utf-8'))
fingerprint=getRandomFingerprint(options)

gl1 = GoLogin({
	"token": token,
	"profile_id": profile_id,
	})
profile1=gl1.getProfile()

# Opening JSON file
f = open('Profile.json')
data = json.load(f)

for x in range(20):
  name='name6'
  startUrl='https://iphey.com/'
  host='193.8.56.109'
  port=9173
  username='phancongvuduc'
  password='phancongvuduc'

  profile1['name']='nameduc'+str(x)
  requests.post(API_URL + '/browser/', headers=headers, json=profile1)
