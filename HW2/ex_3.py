month = int(input('Введите число месяца: '))
my_list = ['winter', 'spring', 'summer', 'autumn']
my_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
if month == 12 or month == 1 or month == 2:
    print(my_dict.get(1))
elif month == 3 or month == 4 or month == 5:
    print(my_dict.get(2))
elif month == 6 or month == 7 or month == 8:
    print(my_dict.get(3))
elif month == 9 or month == 10 or month == 11:
    print(my_dict.get(4))
else:
    print('Такого месяца не существует')