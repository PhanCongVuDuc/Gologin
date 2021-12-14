import requests
import json
import xlrd
import information


start=input('start: ')
end=input('end: ')  
print(str(start)+"-->"+str(end))

# Opening JSON file
f = open(information.my_Profile_path)
profile = json.load(f)

# Give the location of the file
loc = (information.my_InforProfile_path)
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_name('Proxy')



for x in range(int(start)-1,int(end)):
  index=x
  name=sheet.cell_value(index, 8)
  startUrl=''
  host=sheet.cell_value(index, 1)
  port=sheet.cell_value(index, 2)
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
  status=requests.post(information.API_URL + '/browser/', headers=information.get_headers(x+1), json=profile)
  print(str(index+1)+"-Trạng thái: "+ str(status.status_code))