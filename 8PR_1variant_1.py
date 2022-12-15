print('количество строк: ')
n=int(input())
print('введите элементы массива: ')
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append((int(input())))
    a.append(b)
print('массив:')
for i in range(n):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
sum=0
kp=0
for i in range(n):
    for j in range(n):
        if j>i:
            sum=sum+a[i][j]
            if a[i][j]>0:
                kp=kp+1
print('сумма элементов над главной диагональю: ', sum)
print('количество элементов над главной диагональю: ', kp)