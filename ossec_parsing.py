import re

ac=open('alerts')   
son = open('cıktı.txt','w')
data=ac.readlines()
first_format=[]
first_format.append('date,time,devname,type,subtype,level,user,trandisp,transip,app,srcip,srcport,dstip,dstport,dstintf,proto,service,dstcountry,srccountry,action,rcvdbyte,rcvdpkt,appcat,apprisk,applist,dstosname,dstunauthuser,duration,osname,utmaction,srcserver'+'\n')
for i in data:
	date_search=re.search('date=\d+-\d+-\d+',i)
	if date_search:
		date=date_search.group()
		splitted_date= date.split('=')
		first_format.append(splitted_date[1]+',')
	else:
		first_format.append('?,')
		
	time_search=re.search('time=\d+:\d+:\d+',i)
	if time_search:
		time=time_search.group()
		splitted_time= time.split('=')
		first_format.append(splitted_time[1]+',')
	else:
		first_format.append('?,')
		
	devname_search=re.search('devname=\W+\w+',i)
	if devname_search:
		devname=devname_search.group()
		splitted_devname= devname.split('""')
		first_format.append(splitted_devname[1]+',')
	else:
		first_format.append('?,')
			
	type_search=re.search('type=\W+\w+',i)
	if type_search:
		typee=type_search.group()
		splitted_typee= typee.split('""')
		first_format.append(splitted_typee[1]+',')	
	else:
		first_format.append('?,')

	subtype_search=re.search('subtype=\W+\w+\W+\w+',i)
	if subtype_search:
		subtype=subtype_search.group()
		splitted_subtype= subtype.split('""')
		splitted_subtype=splitted_subtype[1].split('"')
		first_format.append(splitted_subtype[0]+',')	
	else:
		first_format.append('?,')
	
	level_search=re.search('level=\W+\w+',i)
	if level_search:
		level=level_search.group()
		splitted_level= level.split('""')
		first_format.append(splitted_level[1]+',')	
	else:
		first_format.append('?,')
		
	
	user_search=re.search('user=\W+\w+.\w+',i)
	if user_search:
		user=user_search.group()
		splitted_user= user.split('""')
		first_format.append(splitted_user[1]+',')
	else:
		first_format.append('?,')
	
	trandisp_search=re.search('trandisp=\W+\w+',i)
	if trandisp_search:
		trandisp=trandisp_search.group()
		splitted_trandisp= trandisp.split('""')
		first_format.append(splitted_trandisp[1]+',')
	else:
		first_format.append('?,')	
		
	transip_search=re.search('transip=\d+.\d+.\d+.\d+',i)
	if transip_search:
		transip=transip_search.group()
		splitted_transip= transip.split('=')
		first_format.append(splitted_transip[1]+',')
	else:
		first_format.append('?,')
	
	app_search=re.search('app=\W+\w+\W+\w+\W+\w+',i)
	if app_search:
		app=app_search.group()
		splitted_app= app.split('""')
		rep=splitted_app[1].replace(',','-')
		rep=rep.replace('"','')
		first_format.append(rep+',')
	else:
		first_format.append('?,')
	
	srcip_search=re.search('srcip=\d+.\d+.\d+.\d+',i)
	if srcip_search:
		srcip=srcip_search.group()
		splitted_srcip= srcip.split('=')
		first_format.append(splitted_srcip[1]+',')
	else:
		srcip_search=re.search('srcip=\w+\d+\W+\w+\d+\w+\d+\W+\d+\w+\W+\w+\d+\W+\w+\d+',i)
		if srcip_search:
			srcip=srcip_search.group()
			splitted_srcip= srcip.split('=')
			first_format.append(splitted_srcip[1]+',')
		else:
			first_format.append('?,')
		
	srcport_search=re.search('srcport=\d+',i)
	if srcport_search:
		srcport=srcport_search.group()
		splitted_srcport= srcport.split('=')
		first_format.append(splitted_srcport[1]+',')
	else:
		first_format.append('?,')
		
	dstip_search=re.search('dstip=\d+.\d+.\d+.\d+',i)
	if dstip_search:
		dstip=dstip_search.group()
		splitted_dstip= dstip.split('=')
		first_format.append(splitted_dstip[1]+',')
	else:
		first_format.append('?,')
	
	dstport_search=re.search('dstport=\d+',i)
	if dstport_search:
		dstport=dstport_search.group()
		splitted_dstport= dstport.split('=')
		first_format.append(splitted_dstport[1]+',')
	else:
		first_format.append('?,')

	dstintf_search=re.search('dstintf=\W+\w+',i)
	if dstintf_search:
		dstintf=dstintf_search.group()
		splitted_dstintf= dstintf.split('""')
		first_format.append(splitted_dstintf[1]+',')
	else:
		first_format.append('?,')		
		
	proto_search=re.search('proto=\d+',i)
	if proto_search:
		proto=proto_search.group()
		splitted_proto= proto.split('=')
		first_format.append(splitted_proto[1]+',')
	else:
		first_format.append('?,')	
		
	service_search=re.search('service=\W+\w+\W+\w+',i)
	if service_search:
		service=service_search.group()
		splitted_service= service.split('""')
		first_format.append(splitted_service[1]+',')
	else:
		first_format.append('?,')	
		
	dstcountry_search=re.search('dstcountry=\W+\w+\W+\w+',i)
	if dstcountry_search:
		dstcountry=dstcountry_search.group()
		splitted_dstcountry= dstcountry.split('""')
		rep=splitted_dstcountry[1].replace(' ','-')
		rep=rep.replace('"','')
		first_format.append(rep+',')
	else:		
		first_format.append('?,')	
		
	srccountry_search=re.search('srccountry=\W+\w+\W+\w+',i)
	if srccountry_search:
		srccountry=srccountry_search.group()
		splitted_srccountry= srccountry.split('""')
		rep=splitted_srccountry[1].replace(' ','-')
		rep=rep.replace('"','')
		first_format.append(rep+',')
	else:
		first_format.append('?,')	
					
	action_search=re.search('action=\W+\w+',i)
	if action_search:
		action=action_search.group()
		splitted_action= action.split('""')
		first_format.append(splitted_action[1]+',')
	else:
		action_search=re.search('action=\W+\w+-\w+',i)
		if action_search:
			action=action_search.group()
			splitted_action= action.split('""')
			first_format.append(splitted_action[1]+',')
		else:
			first_format.append('?,')		
	
	
	rcvdbyte_search=re.search('rcvdbyte=\d+',i)
	if rcvdbyte_search:
		rcvdbyte=rcvdbyte_search.group()
		splitted_rcvdbyte= rcvdbyte.split('=')
		first_format.append(splitted_rcvdbyte[1]+',')
	else:
		first_format.append('?,')	
		
	
	rcvdpkt_search=re.search('rcvdpkt=\d+',i)
	if rcvdpkt_search:
		rcvdpkt=rcvdpkt_search.group()
		splitted_rcvdpkt= rcvdpkt.split('=')
		first_format.append(splitted_rcvdpkt[1]+',')
	else:
		first_format.append('?,')
		
		
	appcat_search=re.search('appcat=\W+\w+\W+\w+',i)
	if appcat_search:
		appcat=appcat_search.group()
		splitted_appcat= appcat.split('""')
		first_format.append(splitted_appcat[1]+',')
	else:
		first_format.append('?,')
			
	apprisk_search=re.search('apprisk=\W+\w+',i)
	if apprisk_search:
		apprisk=apprisk_search.group()
		splitted_apprisk= apprisk.split('""')
		first_format.append(splitted_apprisk[1]+',')
	else:
		first_format.append('?,')		
	
	applist_search=re.search('applist=\W+\w+',i)
	if applist_search:
		applist=applist_search.group()
		splitted_applist= applist.split('""')
		first_format.append(splitted_applist[1]+',')
	else:
		first_format.append('?,')
		
	dstosname_search=re.search('dstosname=\W+\w+',i)
	if dstosname_search:
		dstosname=dstosname_search.group()
		splitted_dstosname= dstosname.split('""')
		first_format.append(splitted_dstosname[1]+',')
	else:
		first_format.append('?,')	
		
	dstunauthuser_search=re.search('dstunauthuser=\W+\w+',i)
	if dstunauthuser_search:
		dstunauthuser=dstunauthuser_search.group()
		splitted_dstunauthuser= dstunauthuser.split('""')
		first_format.append(splitted_dstunauthuser[1]+',')
	else:
		first_format.append('?,')
	
	duration_search=re.search('duration=\d+',i)
	if duration_search:
		duration=duration_search.group()
		splitted_duration= duration.split('=')
		first_format.append(splitted_duration[1]+',')
	else:
		first_format.append('?,')		
		
	osname_search=re.search('osname=\W+\w+',i)
	if osname_search:
		osname=osname_search.group()
		splitted_osname= osname.split('""')
		first_format.append(splitted_osname[1]+',')
	else:
		first_format.append('?,')	

	utmaction_search=re.search('utmaction=\W+\w+',i)
	if utmaction_search:
		utmaction=utmaction_search.group()
		splitted_utmaction= utmaction.split('""')
		first_format.append(splitted_utmaction[1]+'\n')
	else:
		first_format.append('?'+'\n')	
			
son.writelines(first_format)
