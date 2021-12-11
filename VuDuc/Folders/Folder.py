import time
from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

a=json.loads(requests.get(API_URL + '/folders', headers=headers).content.decode('utf-8'))
print(a)
folder=[
  {"name": "1-250",
  "associatedProfiles": []
},
  {"name": "251-500",
  "associatedProfiles": []
},
  {"name": "501-750",
  "associatedProfiles": []
},
  {"name": "751-1000",
  "associatedProfiles": []
},
  {"name": "1001-1250",
  "associatedProfiles": []
},
  {"name": "1251-1500",
  "associatedProfiles": []
},
  {"name": "1501-1750",
  "associatedProfiles": []
},
  {"name": "1751-2000",
  "associatedProfiles": []
},
  {"name": "2001-2250",
  "associatedProfiles": []
},
  {"name": "2251-2500",
  "associatedProfiles": []
},
  {"name": "2501-2750",
  "associatedProfiles": []
},
  {"name": "2751-3000",
  "associatedProfiles": []
},
  {"name": "3001-3250",
  "associatedProfiles": []
},
  {"name": "3251-3500",
  "associatedProfiles": []
},
  {"name": "3501-3750",
  "associatedProfiles": []
},
  {"name": "3751-4000",
  "associatedProfiles": []
},
  {"name": "4001-4250",
  "associatedProfiles": []
},
  {"name": "4251-4500",
  "associatedProfiles": []
},
  {"name": "4501-4750",
  "associatedProfiles": []
},
  {"name": "4751-5000",
  "associatedProfiles": []
},
  {"name": "5001-5250",
  "associatedProfiles": []
},
  {"name": "5251-5500",
  "associatedProfiles": []
},
  {"name": "5501-5750",
  "associatedProfiles": []
},
  {"name": "5751-6000",
  "associatedProfiles": []
},
  {"name": "6001-6250",
  "associatedProfiles": []
},
  {"name": "6251-6500",
  "associatedProfiles": []
},
  {"name": "6501-6750",
  "associatedProfiles": []
},
  {"name": "6751-7000",
  "associatedProfiles": []
},
  {"name": "7001-7250",
  "associatedProfiles": []
},
  {"name": "7251-7500",
  "associatedProfiles": []
},
  {"name": "7501-7750",
  "associatedProfiles": []
},
  {"name": "7751-8000",
  "associatedProfiles": []
},
  {"name": "8001-8250",
  "associatedProfiles": []
},
  {"name": "8251-8500",
  "associatedProfiles": []
},
  {"name": "8501-8750",
  "associatedProfiles": []
},
  {"name": "8751-9000",
  "associatedProfiles": []
},
  {"name": "9001-9250",
  "associatedProfiles": []
},
  {"name": "9251-9500",
  "associatedProfiles": []
},
  {"name": "9501-9750",
  "associatedProfiles": []
},
  {"name": "9751-10000",
  "associatedProfiles": []
},
  {"name": "10001-10250",
  "associatedProfiles": []
},
  {"name": "10251-10500",
  "associatedProfiles": []
},
  {"name": "10501-10750",
  "associatedProfiles": []
},
  {"name": "10751-11000",
  "associatedProfiles": []
},
  {"name": "11001-11250",
  "associatedProfiles": []
},
  {"name": "11251-11500",
  "associatedProfiles": []
},
  {"name": "11501-11750",
  "associatedProfiles": []
},
  {"name": "11751-12000",
  "associatedProfiles": []
},
  {"name": "12001-12250",
  "associatedProfiles": []
},
  {"name": "12251-12500",
  "associatedProfiles": []
},
  {"name": "12501-12750",
  "associatedProfiles": []
},
  {"name": "12751-13000",
  "associatedProfiles": []
},
  {"name": "13001-13250",
  "associatedProfiles": []
},
  {"name": "13251-13500",
  "associatedProfiles": []
},
  {"name": "13501-13750",
  "associatedProfiles": []
},
  {"name": "13751-14000",
  "associatedProfiles": []
},
  {"name": "14001-14250",
  "associatedProfiles": []
},
  {"name": "14251-14500",
  "associatedProfiles": []
},
  {"name": "14501-14750",
  "associatedProfiles": []
},
  {"name": "14751-15000",
  "associatedProfiles": []
},
]
print(type(folder))
print(folder)
for x in folder:
  print(x)
  requests.post(API_URL + '/folders/folder', headers=headers,json=x)


# an={
#   "name": "string",
#   "associatedProfiles": []
# }
# requests.post(API_URL + '/folders/folder', headers=headers,json=an)
