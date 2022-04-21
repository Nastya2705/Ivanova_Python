f_1 = open("my_file.txt", 'x')
str_list = input()
f_1.writelines(str_list)
f_1.close()