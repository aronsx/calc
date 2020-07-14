user_string = input('Введите вырежение: ').split()
# user_string = ['2', '+', '2', '2', '-', '1', '*', '2', '/', '3']
# user_string = ['2', '+', '2', '-', '1', '*', '2', '/', '3']
# user_string = ['2', '+', '2', '*', '2', '*']
# user_string = ['2', '+', '2', '*', '2']


class MathError(Exception):
    pass


try:
    while len(user_string) != 1:
        # первый продод - умножение и деление
        if "*" in user_string or "/" in user_string:  # чтобы не проходить второй раз цикл
            for i, elem in enumerate(user_string):
                if elem.isnumeric() and user_string[i + 1].isnumeric():
                    raise MathError
                if not elem.isnumeric():
                    if elem == '*':
                        r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                        # смещаем индекс влево, так как мы удалили перед ним элемент
                        user_string[i - 1] = str(float(l) * float(r))
                    elif elem == '/':
                        r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                        user_string[i - 1] = str(float(l) / float(r))
        # второй проход - сложнеие и вычитание
        for i, elem in enumerate(user_string):
            if elem == '+':
                r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                user_string[i - 1] = str(float(l) + float(r))
            elif elem == '-':
                r, l = user_string.pop(i + 1), user_string.pop(i - 1)
                user_string[i - 1] = str(float(l) - float(r))


except MathError as me:
    print('Не верное выражение')
except ValueError as ve:
    print(f'Не верное выражение: два оператора подряд')
except IndexError as ie:
    print(f'Не верное выражение: оператор без операнда')

print(f'Результат: {user_string[0] if len(user_string) == 1 else "ошибка вычислений"}')
