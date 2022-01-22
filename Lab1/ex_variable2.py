# Global variable

x = 'MIT'
print(x)


def myfunc():
    # local variable
    x = 'RUTS'
    print(x)


def myfunc2():
    global x
    x = 'Saiyai'
    print(x)

# call myfunc()
myfunc()
print(x)
_x1 = 100
