from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import xlrd
import os



token1= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWMzOGJmZWRkMjVjN2E2ZWExZGI5OTkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWMzOGMwYWRkMjVjNzNlMzkxZGI5YTcifQ.LjbBN8Vb3ZdpHkVxcruthJOa1l1UZOo1cVK_4wJ9J3Y"
token2= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWMzOGNkMWMwYjBkYjIzYjAxMGUzMDQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWMzOGNlMmFjMDE3NjdjYmFiNGQ4Y2QifQ.lJDMrWkF9aXkaUr7FncR4f86O3JM6fICStfL2i5s4Lk"
token3= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWMzOGQ4YjhmZWQ0NzRkM2JhMjdkNWUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWMzOGQ5OGUzNjczZDk2NDQ4OWVmNjEifQ.FdxjzObZsXJjZ5T2505H4SqE8waqalJlPn-AjZp5uQM"
token4= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWMzOGRmOGEyODBmMzFiNTg3M2M3NzYiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWMzOGUwNDQ2Y2MxZjMxMTBlNzI5MWIifQ.vqO_6a1z27-6aYcOKgw-Sgg9VQi-QPSzCbKgxKPLXE8"
token5= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWMzOGVkMTUzNTA3ZTJlNjZlYmQzZjciLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWMzOGVkZWNhNzVkYjI5ZDVjYjI2NzcifQ.qXxqSb5XHFfNZUcxwEPKGTk8pSbXdPO_7wkWxnjJjBQ"
token6= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWM0OWIxMTIzZDc1NGNkOWY3ZTg4OTAiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWM0OWIyMzYyMTg5NzM5Njk5NDhlNzEifQ.eDcV4YktppcdKze7_v2J7JNpENv2MafUzrK1lfy0pX8"
token7= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWM0OWNjMDYyMTg5NzdkNmY5NDkwODQiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWM0OWNjYjViODYzNDdhNTIyMzY2MjIifQ.7i1jsB5sFsb_LMGGDIulF31xMrsUsFZZmV6mcaZ2F1k"
token8= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWM0OWQ3ZmM3MDM1YWExYjZjZDYxODkiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWM0OWRhY2ZjOTkyMmQ0N2I1ZThjYjcifQ.a9K5hVl_GNz1Uw8MdtDAe4IBKSMrLT1m3Itw8IsjrB8"
token9= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWM0ZDhiZjNlMTU1ZTI0ODc1ODgwYjEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWM0ZDhjYzIzZDc1NDFmODU3ZWMwZTEifQ.V7CM3B5yGIQY-L7F7CXHeAEgGlG1b4u__fmLt2oun_4"
token10= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWM0ZDk5MjVjNzNmZDZmZGFlOGVjYWEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWM0ZDk5ZTVjNzNmZDEwMzdlOGVjYmUifQ.eSJ8RWX3ghgaRyoZ6jHZ8g73LvJJubCduZ5Pr0fBCCs"
token11= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWM0ZGE3MTViODYzNDM0OTEyMzljNTUiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWM0ZGE3ZDViODYzNDE4MmYyMzljNzQifQ.QStgp0NEekzII51Sm_GpdzAjTOVrUGYtwD2Z5ETQVRY"
token12= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MWM0ZGFkMWViNzg1Njg0YzI4YTA3MjEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2MWM0ZGFlNTE1YzAwZTdhZDcyOWUwNzUifQ.R9FXwhAZdvqFJ8SEgeZ5IdSIwxdBw_WIt6v8UsgXycM"
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
  elif 10001<=i and i<=11000:
    index=11
  elif 11001<=i and i<=12000:
    index=12
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
  elif 10001<=i and i<=11000:
    index=11
  elif 11001<=i and i<=12000:
    index=12
  return headers[index-1]

# Opening JSON file
f = open(my_Profile_path)
profile = json.load(f)

# Give the location of the file
loc = (my_InforProfile_path)
InforProfile = xlrd.open_workbook(loc)
GetSheetProxy = InforProfile.sheet_by_name('Proxy')





# sheet=['1-1000','1001-2000','2001-3000','3001-4000','4001-5000','5001-6000','6001-7000','7001-8000','8001-9000','9001-10000','10001-11000']


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
  elif index==11:
    result=[10001,11000]
  elif index==12:
    result=[11001,12000]
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
          11:'10001-11000',
          12:'11001-12000',
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
  elif 10001<=i and i<=11000:
    index=11
  elif 11001<=i and i<=12000:
    index=12
  return InforProfile.sheet_by_name(switcher.get(index,"Invalid"))




