import time
from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
import requests
import json
import csv
import xlrd

API_URL = 'https://api.gologin.com'

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWE3N2FjZWU4MjhjOTRmNTA0NzhhMGUifQ.jvQPpHdtwXptJQN5NKySEVpB0JTp8vRmkWR7Z9uUkBs"
profile_id= "61a9d4c3b3e3b34d99607fb9"

headers = {
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Selenium-API'
}
options={
  "token": token,
}

# Give the location of the file
loc = ("Gologin\gologin\VuDuc\InforProfile.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


a=requests.get(API_URL + '/browser/' , headers=headers)
AllProfile=json.loads(a.content.decode('utf-8'))

for x in range(5):
  index=x
  name=sheet.cell_value(index, 6)
  startUrl='https://share-w.in/qdhfqf-41983'
  host=sheet.cell_value(index, 0)
  port=sheet.cell_value(index, 1)
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

gl = GoLogin({
	"token": token,
	"profile_id": profile_id,
	})
profile1=gl.getProfile()
profile1['startUrl']="https://poocoin.app/tokens/0xca1acab14e85f30996ac83c64ff93ded7586977ch"
requests.put(API_URL + '/browser/' + profile_id, headers=headers, json=profile1)
