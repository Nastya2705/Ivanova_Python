def people() :
    name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    both = int(input('Введите год рождения: '))
    city = input('Введите город: ')
    email = input('Введите email: ')
    tel = int(input('Ввидите телефон, начиная с 8: '))
    p_full = [name, last_name, both, city, email, tel]
    return p_full

people_full = people()
print(people_full)
