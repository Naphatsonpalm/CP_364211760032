# while and for loop

"""
พิมพ์ Hello 5 ครั้ง
"""

# while
print('Hello from while loop:')
i = 1
while i <=5:
    print('Hello')
    i+=1

# for
print('Hello from for loop:')
for x in range(5): # 0 1 2 3 4
    print('Hello')

mylist = ['toyota','mazda','honda','nissan','mg','gwm']
# for
for x in mylist:
    if x == 'honda':
        continue
    print(x,type(x))
# while
i = 0
while i < len(mylist):
    pass