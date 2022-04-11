def my_sum():
    result = 0
    ex = False

    while ex == False:
       number = input('введите значения или x для выходв -').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'x':
                ex = True
                break
            else:
                res = res + int(number[el])
        result = result + res
        print(result)
    my_sum()