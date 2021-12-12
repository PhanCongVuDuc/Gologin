import time
from sys import platform
from typing import no_type_check_decorator


import requests
import json
import csv
import xlrd

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

# Opening JSON file
f = open('C:\\Users\\Admin\\Desktop\\Python\\Gologin\\gologin\\VuDuc\\Profile.json')
profile = json.load(f)

# Give the location of the file
loc = ("C:\\Users\\Admin\\Desktop\\Python\\Gologin\\gologin\\VuDuc\\InforProfile.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name('Proxy')

for x in range(730,750):
  index=x
  print(index+1)
  name=sheet.cell_value(index, 8)
  startUrl=''
  host=sheet.cell_value(index, 1)
  port=sheet.cell_value(index, 2)
  username=sheet.cell_value(index, 3)
  password=sheet.cell_value(index, 4)

  profile['name']=name
  profile['proxy']={
    "mode": "socks5",
    "host": host,
    "port": port,
    "username": username,
    "password": password
  }
  profile['startUrl']=startUrl
  requests.post(API_URL + '/browser/', headers=headers, json=profile)
