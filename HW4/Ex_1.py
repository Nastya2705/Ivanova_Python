from sys import argv
name, time, salary, bonus = argv
time = int(time)
salary = int(salary)
bonus = int(bonus)
print(f"Заработная плата: {time*salary + bonus}")


