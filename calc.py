user_string = input('enter expression').split()


# user_string = ['2', '+', '2', '2', '-', '1', '*', '2', '/', '3']
# user_string = ['2', '+', '2', '-', '1', '*', '2', '/', '3']
# user_string = ['2', '+', '2', '*', '2', '*']
# user_string = ['2', '+', '2', '*', '2']


class MathError(Exception):
    pass


try:
    while len(user_string) != 1:
        # first pass: division multiplication
        if "*" in user_string or "/" in user_string:  # not to pass a second time
            for i, elem in enumerate(user_string):
                if elem.isnumeric() and user_string[i + 1].isnumeric():
                    raise MathError
                if not elem.isnumeric():
                    if elem == '*':
                        r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                        # shift the index to the lefT
                        user_string[i - 1] = str(float(l) * float(r))
                    elif elem == '/':
                        r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                        user_string[i - 1] = str(float(l) / float(r))
        # second pass: addition and subtraction
        for i, elem in enumerate(user_string):
            if elem == '+':
                r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                user_string[i - 1] = str(float(l) + float(r))
            elif elem == '-':
                r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                user_string[i - 1] = str(float(l) - float(r))


except MathError as me:
    print('wrong expression')
except ValueError as ve:
    print(f'wrong expression: two operand')
except IndexError as ie:
    print(f'wrong expression: operator without operand')

print(f'result: {user_string[0] if len(user_string) == 1 else "error calculation"}')
