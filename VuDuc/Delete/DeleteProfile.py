import infor

start=int(input('start: '))
end=int(input('end: '))
print(str(start)+"-->"+str(end))

for x in range(start-1,end):
  index=x
  try:
    sock=infor.sheet.cell_value(index, 0)
    id=infor.sheet.cell_value(index, 9)
    infor.delete(id)
    print(index+1)
  except:
    print(str(index+1)+"- An exception occurred")
    

  


