#Draw the sides of the triangle

import math
a= float(input('Please Enter the size of the 1st side of the triangle: '))
b= float(input('Please Enter the size of the 2nd side of the triangle: '))
c= float(input('Please Enter the size of the 3rd side of the triangle: '))
if (a<b+c) and (b<a+c) and (c<a+b):
    print ('A triangle can be drawn with these inputs as sides')

else:
    print ('A triangle cannot be drawn with these sides')

