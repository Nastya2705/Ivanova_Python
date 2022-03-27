i = int(input("Введите целое положительное число: "))
a = 0
while i > 0:
    b = i % 10
    if b >= a:
        a = b
    i //= 10
print("Max: ", a)
