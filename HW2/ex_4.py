my_str = input('Введите строку: ')
world = []
num = 1
for el in range(my_str.count(' ') + 1):
    world = my_str.split()
    if len(str(world)) <= 10:
        print(f'{num} {world[el]}')
        num += 1
    else:
        print(f' {num} {world [el] [0:10]}')
        num += 1
