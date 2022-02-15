# if-else short-hand statement

x = int(input("Enter x integer: "))
y = int(input('Enter y integer: '))
# shorthand if
if x > 100: print('x is more than 100.')

#shorthand if-else
# if x > y:
#     print('x more than y.')
# else:
#     print('x less than y.')
print('x more than y.')if x >y else print('x less than y.')

# shorthand if-else-if
print('x more than y.') if x>y \
    else print('x less than y') if x<y \
    else print('x and y are equal.')