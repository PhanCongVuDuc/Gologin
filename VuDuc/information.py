from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import xlrd
import os
import openpyxl



token1= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI4MGZlN2U5MjM1NzY4OTYxZDU3MWYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI4MTAwOTZiNmU0MDEwMGM2YzYyODIifQ.dgdaSJXNwVeCfz2sZklMxjwBP_5JDc8KDKqr-vkr5XA"
token2= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI4MjNiNzkzNzM0MzkwZDQxMzdkMDgiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI4MjNjN2YzYWQ4Zjk0NWJhNjYxMmQifQ.vk8Go09OekhU5DfBPgOhtQANjnA0zhLEhIFiF1P1V9M"
token3= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI4MjBiNjA0ODAxMDA3NWFjNTUwMzkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI4MjExMjkzNzM0MzgxY2YxMzdhZjkifQ.KCGT1zVG-GS1egHQ_naaf9WDp0dH_J-UjGhZoK01DVA"
token4= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI1ZmVkNGJkNjZmZjFkNzI1NTE3MGMiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI2Njg4NjkwYjAzNzMwMGQ3YTFjMDUifQ.K_L4dD5FDwAmtM1C8Xpt3JwC2xFQxpGvfc6F-DaJYwo"
token5= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI2NjlhZWQwNzk2NDViYTUzODlkYjYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI2NjljMTg4NDNjMTFjNGY5Y2UwNDQifQ.NqxdwKve7gnx9u27CdGZAyTS5UsMeRWvlFhzpYHUvU4"
token6= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI2NmE0Yjc2NWVkODMwNjhlZjQ3OTciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI2NmE1Yjc2NWVkODVlNGFlZjQ3YjIifQ.e627V-jgriXKT_IIwmRsDOw5pDmCClKlUaQg-ORiLow"
token7= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI4MjA2NDkzNzM0MzYwNzQxMzdhN2MiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI4MjA3MWI4Y2I3Y2FiMWFhOTQwMzMifQ.evcuIY9UvoawHDLS4bCTlkGZOySDVZ2QqlBg1JrtuCs"
token8= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI2ZGYwOWE3ZjAwM2QzY2ZjMTI2NzgiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI2ZGYxMzRjOGU4ODE4YzZkMDc1ZjcifQ.mgIbN1DPG6GTuM3Yybd0G4WPla94JZwLAi-0pa6Jox8"
token9= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWI4M2E5NWI4Y2I3YzZmMzFhOTU2YzkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWI4M2FhMmI4Y2I3YzdlNzJhOTU2ZGMifQ.ikgX4tkBdkpzPJ-7_56bVIuE3KWQJ-nTySngHq34s04"
token10= ""
token11= ""
token12= ""
tokens=[token1,token2,token3,token4,token5,token6,token7,token8,token9,token10,token11,token12]

def get_tokens(i):
  if 1<=i and i<=1000:
    index=1
  elif 1001<=i and i<=2000:
    index=2
  elif 2001<=i and i<=3000:
    index=3
  elif 3001<=i and i<=4000:
    index=4
  elif 4001<=i and i<=5000:
    index=5
  elif 5001<=i and i<=6000:
    index=6
  elif 6001<=i and i<=7000:
    index=7
  elif 7001<=i and i<=8000:
    index=8
  elif 8001<=i and i<=9000:
    index=9
  elif 9001<=i and i<=10000:
    index=10
  return tokens[index-1]


my_vuduc_folder_path = os.path.abspath(os.path.dirname(__file__))
my_InforProfile_path = os.path.join(my_vuduc_folder_path, "InforProfile.xlsx")
my_Profile_path = os.path.join(my_vuduc_folder_path, "Profile.json")


API_URL = 'https://api.gologin.com'

headers=list()
for token in tokens:
  header = {
  'Authorization': 'Bearer ' + token,
  'User-Agent': 'Selenium-API'
  }
  headers.append(header)

def get_headers(i):
  if 1<=i and i<=1000:
    index=1
  elif 1001<=i and i<=2000:
    index=2
  elif 2001<=i and i<=3000:
    index=3
  elif 3001<=i and i<=4000:
    index=4
  elif 4001<=i and i<=5000:
    index=5
  elif 5001<=i and i<=6000:
    index=6
  elif 6001<=i and i<=7000:
    index=7
  elif 7001<=i and i<=8000:
    index=8
  elif 8001<=i and i<=9000:
    index=9
  elif 9001<=i and i<=10000:
    index=10
  return headers[index-1]

# Opening JSON file
f = open(my_Profile_path)
profile = json.load(f)

# Give the location of the file
loc = (my_InforProfile_path)
InforProfile = xlrd.open_workbook(loc)
GetSheetProxy = InforProfile.sheet_by_name('Proxy')





sheet=['1-1000','1001-2000','2001-3000','3001-4000','4001-5000','5001-6000','6001-7000','7001-8000','8001-9000','9001-10000']


def get_doan_proxy(index):
  result=list()
  if index==1:
    result=[1,1000]
  elif index==2:
    result=[1001,2000]
  elif index==3:
    result=[2001,3000]
  elif index==4:
    result=[3001,4000]
  elif index==5:
    result=[4001,5000]
  elif index==6:
    result=[5001,6000]
  elif index==7:
    result=[6001,7000]
  elif index==8:
    result=[7001,8000]
  elif index==9:
    result=[8001,9000]
  elif index==10:
    result=[9001,10000]

  return result

def get_sheet_with_stt(i):
  switcher={
          1:'1-1000',
          2:'1001-2000',
          3:'2001-3000',
          4:'3001-4000',
          5:'4001-5000',
          6:'5001-6000',
          7:'6001-7000',
          8:'7001-8000',
          9:'8001-9000',
          10:'9001-10000',
        }
  index=0
  if 1<=i and i<=1000:
    index=1
  elif 1001<=i and i<=2000:
    index=2
  elif 2001<=i and i<=3000:
    index=3
  elif 3001<=i and i<=4000:
    index=4
  elif 4001<=i and i<=5000:
    index=5
  elif 5001<=i and i<=6000:
    index=6
  elif 6001<=i and i<=7000:
    index=7
  elif 7001<=i and i<=8000:
    index=8
  elif 8001<=i and i<=9000:
    index=9
  elif 9001<=i and i<=10000:
    index=10
  return InforProfile.sheet_by_name(switcher.get(index,"Invalid"))




