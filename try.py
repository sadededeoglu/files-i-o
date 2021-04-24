yaz=open('temz.txt','w') 
karisik=['a','b','c','d','e','q']
alerts=['d','e','a','q']
arr=[]
for i in karisik: 
  varMi = False 
  for j in alerts:
    if(i == j): 
      varMi = True 
      if(varMi == False): 
        arr.append(i+'\n')
yaz.writelines(arr) 
