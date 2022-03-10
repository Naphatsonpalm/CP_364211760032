# Function


print('Start')

def myfuncA():
    print('Hello A')

def myfuncB(x):
    print('Hello B',x)

def myfucnC(x,y):
    print('Hello C',(x+y))

def myfucnD(*x): # x --> tuple
    print(x)
    total = 0
    for i in x:
        print(i, end=" ")
        total += i
    # return total value
    return total
# keyword
def myfucnE(x,y,z):
    print(f'x={x} y={y} z={z}')
    print(f'summation of value is : {x+y+z}')

def myfuncF(**num): # num--> dictionary
    for x in num.items():
        print(x)
    t = 0
    for x in num.values():
        t += x
    print(f'totoal value from myfuncF: {t}')

# default parameter
def myfuncG(country = 'Thailand'):
    print(country)


# calling function
myfuncA()
myfuncB(100)
myfucnC(100,200)
print('total value: ',myfucnD(100,200,300,400,500))
re = myfucnD(100,200,300,400,500)
print(re)
# keyword arugeument
myfucnE(z=100,x=200,y=300)
myfuncF(num1=100,num2=200,num3=300)
# default parameter
myfuncG()
myfuncG('Maylasia')
myfuncG('Russia')



print('\nEnd')