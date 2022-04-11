var_1 = int(input('Введите число'))
var_2 = int(input('Введите число'))
var_3 = int(input('Введите число'))
def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return var_1 + var_2
    elif var_2 >= var_1 and var_3 >= var_1:
        return var_2 + var_3
    else:
        return var_1 + var_3

print(my_func(var_1, var_2, var_3))