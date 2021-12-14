from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import xlrd

API_URL = 'https://api.gologin.com'

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI4MGY1N2YzYWQ4ZjZiOTFhNjRlN2IiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI4MGY2ODA4ZTg0MTFhOWQzMDMzYTUifQ.LHiIxQk4RTZ5hDuDw0yYjNpk-V7wZVmG9I6R2UY74Ow"

headers = {
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Selenium-API'
}
options={
  "token": token,
}

# Give the location of the file
loc = ("C:\\Users\\Admin\\Desktop\\VuDuc\\Gologin\\gologin\\VuDuc\\InforProfile.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name('Proxy')

def delete(id):
  return requests.delete(API_URL + '/browser/' + id, headers=headers)