import infor

start=int(input('start: '))
end=int(input('end: '))
print(str(start)+"-->"+str(end))

for x in range(start,end):
  index=x

  error=infor.sheet.cell_value(index, 8)
  if error==31 or error==1:
    try:
      sock=infor.sheet.cell_value(index, 0)
      id=infor.sheet.cell_value(index, 7)
      infor.delete(id)
      print(index+1)
    except:
      print(str(index+1)+"- An exception occurred")

  


