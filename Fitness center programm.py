age=int(input("what is your age"))
if age<18:
    print('You are eligible for the Teens Fitness Program')
elif age>=18 and age<=40:
    print('You are eligible for the regular fitness Program')
else:
    print('You are eligible for the senior Wellness Program')
medical_condition=input('Do you have any medical condition? ').strip().lower()
if medical_condition!='yes' and medical_condition!='no':
 print('Invalid input.Please enter No or Yes.')
elif  medical_condition=='yes' and age>=40:
    print("Medical Clearance required before joining.")
elif age<40 or medical_condition=='no':
    print('You can proceed with registration.')
membership_type=input("what membership type do you require? ").strip().lower()
membership1='basic'
membership2='premium'
if membership_type=="basic":
    answer=input('Do you want personal training? ').strip().lower()
    if answer=='yes':
        print('Basic plan with pesronal training: $45 per month.')
    if answer=='no':
     print('Basic plan:$30 per month')
if membership_type=='premium':
    print('Premium plan:$60 per month.')
    if membership_type=='premium' and age<30:
       print("You qualify for a youth discount! 10% off your plan.")