from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import xlrd

linkref='https://share-w.in/f5huty-42970'

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

# Opening JSON file
f = open('C:\\Users\\Admin\\Desktop\\VuDuc\\Gologin\\gologin\\VuDuc\\Profile.json')
profile = json.load(f)

# Give the location of the file
loc = ("C:\Users\\Admin\\Desktop\\VuDuc\\Gologin\\gologin\\VuDuc\\InforProfile.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name('Proxy')

def update(id):
  profile_temp=json.loads(requests.get(API_URL + '/browser/' + id, headers=headers).content.decode('utf-8'))
  profile_temp['storage']= {"local": True, "extensions": True, "bookmarks": True, "history": True, "passwords": True, "session": False}
  profile_temp['startUrl']=linkref
  requests.put(API_URL + '/browser/' + id, headers=headers, json=profile_temp)

def updateName(id,name):
  profile_temp=json.loads(requests.get(API_URL + '/browser/' + id, headers=headers).content.decode('utf-8'))
  profile_temp['name']=name
  profile_temp['startUrl']=linkref
  requests.put(API_URL + '/browser/' + id, headers=headers, json=profile_temp)