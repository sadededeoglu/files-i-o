import re
ac=open('first.txt','r')
yaz=open('alert.txt','w')
data=ac.readlines()
over=[]
for i in data:
  try:
    sil2=re.findall(',ccode=\S+,,',i)[0]
    if sil2: sa=i.replace(sil2,'')
      sa=sa.replace('""','"')
      over.append(sa+'\n')
  except IndexError:
    pass
yaz.writelines(over)
