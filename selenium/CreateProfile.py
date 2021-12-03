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


name='name6'
startUrl='https://iphey.com/'

def getRandomFingerprint(options):
  os_type = options.get('os', 'lin')
  return json.loads(requests.get(API_URL + '/browser/fingerprint?os=' + os_type, headers=headers).content.decode('utf-8'))
fingerprint=getRandomFingerprint(options)

host='193.8.56.109'
port=9173
username='phancongvuduc'
password='phancongvuduc'



# print(type(fingerprint))
# with open('fingerprint.json', 'w') as f:
# 	json.dump(fingerprint, f)
# 	print('Done Json')

profile={
  "name": name,
  "notes": "auto generated",
  "browserType": "chrome",
  "os": "lin",
  "devicePixelRatio": 1,
  "startUrl": startUrl,
  "googleServicesEnabled": False,
  "lockEnabled": True,
  "debugMode": False,
  "navigator": fingerprint.get('navigator', {}),
  "storage": {
    "local": True,
    "extensions": True,
    "bookmarks": True,
    "history": True,
    "passwords": True,
    "session": True
  },
  "proxyEnabled": True,
  "proxy": {
    "mode": "socks5",
    "host": host,
    "port": port,
    "username": username,
    "password": password
  },
  # "dns": "string",
  "plugins": {
    "enableVulnerable": True,
    "enableFlash": True
  },
  "timezone": {
    "enabled": True,
    "fillBasedOnIp": True,
    # "timezone": "string"
  },
  # "geolocation": {
  #   "country": "string",
  #   "region": "string",
  #   "city": "string",
  #   "timezone": "string"
  # },
  "audioContext": {
    "mode": "noise",
    # "noise": 0
  },
  "canvas": {
    "mode": "off",
    # "noise": 0
  },
  "fonts": {
    "families": fingerprint.get('fonts'),
    "enableMasking": True,
    "enableDomRect": True
  },
  "mediaDevices": {
    "videoInputs": 1,
    "audioInputs": 1,
    "audioOutputs": 1,
    "enableMasking": True
  },
  "webRTC": {
    "mode": "alerted",
    "enabled": True,
    "customize": True,
    "localIpMasking": True,
    "fillBasedOnIp": True,
    # "publicIp": "string",
    # "localIps": [
    #   "string"
    # ]
  },
  # "webGL": {
  #   "mode": "noise",
  #   "getClientRectsNoise": 0,
  #   "noise": 0
  # },
  # "webGLMetadata": {
  #   "mode": "mask",
  #   "vendor": "string",
  #   "renderer": "string"
  # },
  # "webglParams": {},
  # "extensions": {
  #   "enabled": True,
  #   "preloadCustom": True,
  #   "names": [
  #     "string"
  #   ]
  # },
}


# gl = GoLogin(options)
# requests.post(API_URL + '/browser/', headers=headers, json=profile)


gl1 = GoLogin({
	"token": token,
	"profile_id": profile_id,
	})
profile1=gl1.getProfile()

# Opening JSON file
f = open('Profile.json')
data = json.load(f)


profile1['name']='name11'
requests.post(API_URL + '/browser/', headers=headers, json=profile1)
