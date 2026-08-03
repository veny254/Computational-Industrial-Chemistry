import matplotlib.pyplot as plt
moles=float(input('enter the initial number of moles   '))
volume=float(input('enter the volume in litres   '))
target=''
while target!='ideal' and target!='real':
    target=input('choose the target gas  ').strip().lower()
list=[0,10,20,30,40,50,60,70,80,90,100]
k=273.15
R=0.08206
a=3.592
b=0.04267
for t in list:
 T=t+k
 print(T)
 if target=='real':
  pressure=((moles*R*T)/(volume-(moles*b)))-((a*(moles**2))/(volume**2))
  if pressure<1.0:
     print('low vacuum pressure detected')
  if pressure>=1.0 and pressure<=12.0:
     print(pressure) 
  if pressure>12.0:
     print('High  critical pressure detected')  
     break
 if target=='ideal':
  P=(moles*R*T)/volume
  if P<1.0:
     print('Low  vacuum pressure detected')
  if P>=1.0 and P<=12.0:
     print(P)
  if P>12.0:
     print('High critical pressure detected')  
     break 