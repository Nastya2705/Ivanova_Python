arg_1 = int(input('Введите первое значение: '))
arg_2 = int(input('Введите второе значение: '))
def my_div(arg_1, arg_2):
        if arg_2 == 0:
            print('Делить на ноль нельзя.')
        else:
            return arg_1 / arg_2

print(my_div(arg_1, arg_2))
