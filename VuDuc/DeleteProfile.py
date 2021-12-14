import information
import requests
import xlrd

start=int(input('start: '))
end=int(input('end: '))
print(str(start)+"-->"+str(end))

# Give the location of the file
loc = (information.my_InforProfile_path)
wb = xlrd.open_workbook(loc)
sheet_proxy = wb.sheet_by_name('Proxy')

def delete(API_URL,headers,id):
  requests.delete(API_URL + '/browser/' + id, headers=headers)

for x in range(start-1,end):
  index=x
  try:
    id=sheet_proxy.cell_value(index, 9)
    status=requests.delete(information.API_URL + '/browser/' + id, headers=information.get_headers(x+1))
    print(str(index+1)+"-Trạng thái: "+ str(status.status_code))
  except:
    print(str(index+1)+"- Delete lỗi")
    

  


