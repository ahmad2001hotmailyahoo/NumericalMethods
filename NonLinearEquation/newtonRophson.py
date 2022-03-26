from ast import Str
from tokenize import String
import equationSol
from sympy import lambdify


a = equationSol.getInput()
intialGuess = 0

intialGuess = equationSol.checkFunction(intialGuess)
initialGuess = equationSol.checkDerivative(intialGuess)

while(equationSol.derivativeOfFunction(intialGuess) == 0 ):
    intialGuess = intialGuess + 1
    print(intialGuess)
x = intialGuess
print(x)


for i in range(0,101,1):
    fofx = equationSol.evaluate(x) 
    derivativeOfFOfx = equationSol.derivativeOfFunction(x)
    print(f'After {i}th iteration')
    print(x)
    print(f'x = {float(x)} | f(x) = {(fofx)} | f`(x) = {derivativeOfFOfx} |', end ="")   
    xp = x 
    x = x - (fofx/derivativeOfFOfx)
    print(f'x(i+1) = {float(x)} | f(x(i+1)) = {float(equationSol.evaluate(x))} | x(i+1) - x(i) = {float(x - xp)}')
    if((x-xp)*100 < 1 and (x-xp)*100 > -1 ): break


print("The value of x is : ", float(x))