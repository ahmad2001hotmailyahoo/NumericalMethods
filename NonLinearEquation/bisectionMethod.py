from sympy import solve
import equationSol

a = 0 
b = 0
c = 0


equationSol.getInput()

while True :
    print("Guess must be such that one value gives negative answer and other gives positive answer" )
    a = float(input("Enter the first intial guess"))
    b = float(input("Enter the seconed initial guess"))

    if(equationSol.validateFunction(a) and equationSol.validateFunction(b) and equationSol.validateFunction(a+b)):
        if(equationSol.evaluate(a)*equationSol.evaluate(b) < 0):
            break 
        else:
            print("The following values doest give anser of differnt signs")
    else :
        print('The Function in not defined at any or both the inputs try another guess')

for i in range(100):
    c = (a+b)/2
    print(f'After {i}th iteration : ')
    print( ' a = ' , a ,' | ', ' b = ', b , ' | ' , ' c = ',  c , ' ' , ' | ' , ' ' , 'f(a) = ', equationSol.evaluate(a),  ' ' ,' | ' , ' ' , 'f(b) = ' ,equationSol.evaluate(b) ,  ' ' ,' | ' , ' ' , ' f(c) = ' , equationSol.evaluate(c))
    if (equationSol.evaluate(c) * 1000 < 1 and equationSol.evaluate(c) * 1000 > -1):
        break 
    if(equationSol.evaluate(a)*equationSol.evaluate(c) < 0):
        b = c
    elif(equationSol.evaluate(b)* equationSol.evaluate(c) < 0):
        a = c  


print('The answer is ' , c)