import time
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from gologin import GoLogin
import requests
import json
import csv
import openpyxl


API_URL = 'https://api.gologin.com'

token= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MTc4ZDEyMDM0MWY2OGY1YzlmYjQzYTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI1ZmFjMjQyZTZiZTgyZDk0Y2JkNjEifQ.WX8JjT9JBR2SivmLuoLOG7k2QhRqeM6rEz-8bgJv7_k"

headers = {
	'Authorization': 'Bearer ' + token,
	'User-Agent': 'Selenium-API'
}


a=requests.get(API_URL + '/browser' , headers=headers)
data=json.loads(a.content.decode('utf-8'))


filename='C:\\Users\\Admin\\Desktop\\Python\\Gologin\\gologin\\VuDuc\\InforProfile.xlsx'

wb=openpyxl.load_workbook(filename)
sheet1=wb['Data']
sheet1.delete_cols(1,2)

row=1
for x in data:
	proxy=x['proxy']
	name=x['id']

	host=proxy['host']
	sheet1.cell(row,1).value=host
	sheet1.cell(row,2).value=name

	row=row+11


wb.close()
wb.save(filename)


# with open('GetAllProfile.json', 'w') as f:
# 	json.dump(b, f)
# 	print('Done Json')