ac=open('karisikraw.txt','r') 
ac2=open('temizalert.txt','r')
yaz=open('temz.txt','w')
karisik=ac.readlines()
alerts=ac2.readlines()
arr=[]
for i in karisik:
  varMi = False
  for j in alerts:
    if(i == j):
      varMi = True
      if(varMi == False):
        arr.append(i)
yaz.writelines(arr) 
