x = []
y = []
for i in range(10):
    x.append(int(input('Введиите числа\n')))
    print(x)
for i in range(10):
    if x[i]<0:
        y.append(x[i])
        y.sort()
print(y)