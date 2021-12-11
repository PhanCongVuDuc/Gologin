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
import threading
import time

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

# Give the location of the file
loc = ("InforProfile.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)


# AllProfile=json.loads(requests.get(API_URL + '/browser/' , headers=headers).content.decode('utf-8'))

def delete(id):
  requests.delete(API_URL + '/browser/' + id, headers=headers)

# Opening JSON file
f = open('Profile.json')
profile = json.load(f)

# Give the location of the file
loc = ("InforProfile.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)




for x in range(0,750):
  index=x
  print(index+1)

  try:
    delete(sheet.cell_value(index, 7))
  except:
    print("An exception occurred")

  # thread1=threading.Thread(target=update,args=(x['id'],))
  # thread1.start()
  # thread1.join()

