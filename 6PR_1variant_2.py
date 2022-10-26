from random import randint
x = [randint(1,10) for i in range(10)]
max_x=max(x)
print(x)
print('Наибольшее число идёт под номером', 1 + (x.index(max_x)))