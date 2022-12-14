# Calculate the Average

import math
a= input('Please Enter Your First Name: ')
b= input('Please Enter Your Last Name: ')
x= float(input('Enter the Grade of your 1st Course: '))
y= float(input('Enter the Grade of your 2nd Course: '))
z= float(input('Enter the Grade of your 3rd Course: '))
print('First Name: ',a)
print('Last Name: ',b)
average=float((x+y+z)/3)

print ('Average:' ,average)

if average>=17:
    print('Congratulations, Average status: Great ')

if average<17 and average>=12:
    print('Average status: Normal ')

if average<12:
    print('Unfortunately, Average status: Fail ')