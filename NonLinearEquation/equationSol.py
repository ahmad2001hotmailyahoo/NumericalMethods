from cmath import *
from scipy.misc import derivative
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy import diff, Symbol,solve,lambdify

var1 = 0 

equation = ""

def getInput():
    global equation
    equation = input("Enter The equation(the unknown can be only x)");
    return equation


def validateFunction(y):
    print(equation)
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(equation, my_symbols)
    my_func = lambdify(my_symbols['x'], my_func)
    try :
        my_func(y)
        return true 
    except:    
        return false



def checkFunction(y):
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(equation, my_symbols)
    my_func = lambdify(my_symbols['x'], my_func)
    for i in range(100):
        try :
            y = y + 1
            my_func(y)
            break 
        except:    
            print('notWrite')

    return y

def checkDerivative(y):
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(equation, my_symbols)
    f_prime = diff(my_func, my_symbols['x'])
    f_prime = lambdify(my_symbols['x'], f_prime)

    for i in range(100):
        try :
            y = y + 1
            f_prime(y)  
            break 
        except:    
            print('notWrite')
            
            
 
    return y



def evaluate(y):
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(equation, my_symbols)
    my_func = lambdify(my_symbols['x'], my_func)
    return my_func(y)


def derivativeOfFunction(y):
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(equation, my_symbols)
    f_prime = diff(my_func, my_symbols['x'])
    f_prime = lambdify(my_symbols['x'], f_prime)
    return f_prime(y)





