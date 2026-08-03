#This program calculates the number of moles of an  pressure of a gas using ideal gas law and real
user=input('What is your name? ').strip()
gas=(input("which gas do you want to calculate pressure?   "))
mass=float(input("what is i'ts the mass in grams?   "   ))
molar_mass=float(input("what is i'ts  molar mass in g/mol?  "   ))
moles=mass/molar_mass
print("moles of",gas,'is:',round(moles,4))
R=float(input('constant value') )#atm.L/mol.K
temperature=float(input("Temperature:")) #in degrees celcius
T=temperature+273
V=float(input("Volume in litres:"))  #Volume of gas in Litres
P=(moles*R*T)/V # pressure measured in atmosphere
print('Ideal  pressure of',gas,'is',round(P,4),'atm')
a=float(input('value of a:'))
b=float(input('value of b:'))
PR=((moles*R*T)/(V-moles*b))-((a*moles**2)/(V**2))
print('Real pressure of',gas,'is:',round(PR,4),'atm')
error=''
while error!='yes' and error!='no':
 error=input('Do you want to calculate percentage error? ').strip().lower()
 if error!='yes' and error!='no':
    print('Invalid input answer (yes or no)')
if error=='yes':
    deviation=P-PR
    percentage_error=(deviation/PR)*100
    print('percentage error is:',round(percentage_error,4),'%.Welcome again' ,user)
if error=='no':
         print('Bye! Bye! Feel free to come back',user)