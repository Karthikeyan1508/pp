num_list = [1,2,3,4,5,6,7,8,9,10]
num_list[10]

#     num_list[10]
#     ~~~~~~~~^^^^
# IndexError: list index out of range

# ---------------------------------------------------------------

int('67.5')

#     int('67.5')
# ValueError: invalid literal for int() with base 10: '67.5'

# ---------------------------------------------------------------

a = 2
b = 'Data'

result = a + b

#     result = a + b
#              ~~^~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ---------------------------------------------------------------

if(amount > 1000)
    print('Amount is greater than 1000')

#     if(amount > 1000)
#                      ^
# SyntaxError: expected ':'