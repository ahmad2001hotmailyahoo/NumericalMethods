#This is Euler method program
import math

h = float(input("Enter the hieght of interval"))
noOfDecimalPlaces = 
fxy = input("Enter the function")
x = float(input("Enter the initial value"))
y = float(input('Enter the initial answer'))
yNext = 0
xn = float(input('Enter the value at which you want to value of function'))

print('xi     |   yi    |   yi+1 '  )
while(x <= xn):
    yNext = y + h * eval(fxy)
    print(f'{x}    |   {y}   |   {yNext} '  )
    x = x + h 
    y = yNext
