import information

start=int(input('start: '))
end=int(input('end: '))
print(str(start)+"-->"+str(end))

for x in range(start,end):
  index=x

  error=information.sheet.cell_value(index, 8)
  if error==31 or error==1:
    try:
      sock=information.sheet.cell_value(index, 0)
      id=information.sheet.cell_value(index, 9)
      information.delete(id)
      print(index+1)
    except:
      print(str(index+1)+"- An exception occurred")

  


