import re
ac=open('raw_ve_alert')
yaz=open('rawlar.txt','w')
data=ac.readlines()

over=[]
for i in data:
	sil=re.search('\d+,"',i)
	if sil:
		silmek=sil.group()
		s=i.replace(silmek,'')
		sil2=re.search(',ccode=""ZFR""",\d+\W+\d+\W+\d+',s)
		if sil2:
			silmek2=sil2.group()
			sa=s.replace(silmek2,'')
			sa=sa.replace('""','"')
			sa=sa.replace('"""','"')
			over.append(sa+'\n')	
		else:
			sil2=re.search(',\d+\W+\d+\W+\d+',s)
			if sil2:
				silmek2=sil2.group()
				sa=s.replace(silmek2,'')
				sa=sa.replace('""','"')
				sa=sa.replace('"""','"')
				over.append(sa+'\n')
yaz.writelines(over)
