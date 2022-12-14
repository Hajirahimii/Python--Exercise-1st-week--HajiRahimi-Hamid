# Create calculator

import math
a= int(input('Please Enter 1st Number: '))
b= int(input('Please Enter 2nd Number: '))

op= input ('Please Enter Operation: ')

if op == '+':
    result=a+b
if op == '-':
    result=a-b

if op == '*':
    result=a*b

if op == '/' and  b == 0:  
   result= ('= Error') 
#else:
if op == '/' and  b != 0:  
    result=a/b

print ('The result is: ' ,result)



    #result=a/b

#if op == 'sqrt':
 #   result=a/b

#print(result)

##################################################################################################

x=float(input('For sqrt: Please Enter Number =  ' ))
square_root = math.sqrt(x)
print('The Sqrt of (', x,') is = ' , square_root)

###################################################################################################

Degree= float(input('For Calculate Trigonometry (sin/cos/tan/cot): Please Enter Degree: '))

theta1=math.sin(math.radians(Degree))
print ('sin(', Degree ,') =' , theta1)

theta2=math.cos(math.radians(Degree))
print ('cos(', Degree ,') =' , theta2)

theta3=math.tan (math.radians(Degree))
print ('tan(', Degree ,') =' , theta3)

if theta3==0:
    print ('(cot)(', Degree ,') = Infinite Amount')
else:
    theta4= (1/theta3)
    print ('cot(', Degree ,') =' , theta4)

##################################################################################################

factorial=int(input('Please Enter Number to Calculate Factorial:'))
f=math.factorial(factorial)
print('The Factorial of ' , factorial, 'is : ' , f)