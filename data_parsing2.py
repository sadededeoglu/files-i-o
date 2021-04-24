import re
ac=open('alarmlar','r')
yaz=open('ilk.txt','w')
data=ac.readlines()
over=[]
for i in data:
  try:
    sil2=re.findall('\d+,\d+\S+"',i)[0]
    if sil2:
      sa=i.replace(sil2,'')
      over.append(sa+'\n')
      except IndexError:
        pass 
yaz.writelines(over)
