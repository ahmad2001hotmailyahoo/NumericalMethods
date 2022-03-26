import equationSol

print("Enter the equation terms of Φ(x)")
equationSol.getInput()

n = int(input("Enter the no. of iteration"))
e = float(input("Enter the minimuum accuracy"))
e = 10 ** e 
x0 = 0 
x1 = 0 

for i in range(n):
    print(f"iteration No. {i}")
    x1 = equationSol.evaluate(x0)
    print(f'x0 = {x0} | x1 = {x1}',end=" | ")
    print(f'x1-x0 = {x1-x0}')
    if ((x1 - x0) * e)  < 1 and  ((x1 - x0) * e)  > -1:
        break 
    x0 = x1


print(f'The value of x is {x1}')

