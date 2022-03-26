import numpy

while True:
    f0 = int(input('Enter the first value'))
    fn = int(input('Enter the last value'))
    h  = int(input('Enter the lenght of interval'))
    print((fn-f0)/h)
    if(((fn-f0)/h)%1==0):
        break
    else:
        print('Enter Valid hieght')
        continue


size = (fn-f0)/h
answerOfFunction= numpy.array((),dtype=float)
answerOfFunction.resize(int(size))

for i in range(int(size)):
    if(not ( i == 0 or i == size - 1 ) ):
        answerOfFunction[i] = float(input(f'Enter the {i+1} value'))


answer = 0 
for i in range(int(size)):
    if(i==0):
        answer =  answer + f0
    elif(i==size-1):
        answer =  answer + fn
    else:
        answer = answer + 2*answerOfFunction[i]

print(f'The answer of integration is: {h*answer/2}')