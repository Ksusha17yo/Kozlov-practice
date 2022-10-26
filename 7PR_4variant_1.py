x = []
y = []
for i in range(10):
    x.append(int(input('Введите числа\n')))
print(x)
for i in range(10):
    if x[i] % 2 != 0:
        y.append(x[i])
if y == []:
    print('Все числа чётные')
else:
    y.sort(reverse=True)
    print(y)