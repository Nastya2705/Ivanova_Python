f_1 = open("file.txt", 'r')
content = f_1.read ()
print(f'Содержание файла: {content}')
f_1 = open("file.txt", 'r')
content =f_1.readlines()
print(f'количество строк в файле - {len(content)}')
f_1 = open("file.txt", 'r')
content =f_1.readlines()
for i in range(len(content)):
    print(f'rjkdj cbvdjkjd{i+1} -jq xnhjrb {len(content)}')
f_1 = open("file.txt", 'r')
content = f_1.read()
content = content.split()
print(f'Общее колво слов - {len(content)}')
f_1.close()
