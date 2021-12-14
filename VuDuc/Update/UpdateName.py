import time
from sys import platform
from typing import no_type_check_decorator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import csv
import xlrd
import threading
import time
import information

start=input('start: ')
end=input('end: ')  
print(str(start)+"-->"+str(end))


for x in range(int(start),int(end)):
  index=x
  try:
    information.updateName(information.sheet.cell_value(index, 9),information.sheet.cell_value(index, 10))
    print(index+1)
  except:
    print(str(index)+" An exception occurred")



