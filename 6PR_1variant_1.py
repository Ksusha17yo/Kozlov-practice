def zam(x):
  appa = 0
  for i in range(5):
    appa += x[i]
  print('Сумма элементов', appa)
  appa = appa/5
  print('Среднеарифметичсекое ', appa)
  return appa
def spam(y):
  appa = 0
  for i in range(5):
    appa += y[i]
  print('Сумма элементов', appa)
  appa = appa/5
  print('Среднеарифметичсекое ', appa)
  return appa
def cam(w):
  appa = 0
  for i in range(5):
    appa += w[i]
  print('Сумма элементов', appa)
  appa = appa/5
  print('Среднеарифметичсекое ', appa)
  return appa
A = []
for i in range(5):
  A.append(int(input('Введите элемент 1 массива')))
B = []
for i in range(5):
  B.append(int(input('Введите элемент 2 массива')))
C = []
for i in range(5):
  C.append(int(input('Введите элемент 3 массива')))
print(zam(A))
print(spam(B))
print(cam(C))