from sys import float_repr_style
from typing import List
import numpy

n = 0 
def inputNoOfEquation():
    global n
    n = int(input('Enter the no. equation'))
inputNoOfEquation()
equations = numpy.array((),dtype=float)
equations.resize((n,n+1))
equation = numpy.array((),dtype = float)
equation.resize((n+1))
expression = '' 

def getVar(expression):
    index = 0
    f = ''
    n=''
    check = False
    chech1 =True
    for j in expression:
        if(j =='-' and chech1): 
            n = '-'
            chech1 = False
        elif j.isdigit() :
            check = True
            f += j
            continue
        elif j.isalpha() and check == False :
            check = True
            f = '1'
        if(check):
            equation[index] = int(f)
            f = ''
            if(not chech1): 
                equation[i]=equation[index]*-1
            index = index + 1 
            check = False
            chech1= True
    equation[index] = int(f) 
    return equation



for i in range (n):
    print(f'Enter the {i+1}th equation: ')
    expression = input()
    equation = getVar(expression)
    equations[i] = equation

equation1 = numpy.array((),dtype = float)
equation1.resize((n))
equation2 = numpy.array((),dtype = float)
equation2.resize((n))

for i in range(n):
    equation1[i] = 0
    equation2[i]=0
x = 0 
y = 0

for k in range(100):
    for i in range(0,n):
        y = 0 
        for j in range(0,n+1):
            if(i == j):
                x = equations[i][j]
            elif(i!=j and j != n ):
                y = y - equation1[j]  * equations[i][j]
            elif(j == n):
                y = y + equations[i][j]
                equation1[i] = y/x
        equation2 = equation1

        

print(equation1)