print('количество столбцов: ')
n=int(input())
print('количество строк: ')
m=int(input())
print('ведите элементы: ')
a=[]
for i in range(n):
    b=[]
    for j in range(m):
        b.append((int(input())))
    a.append(b)
print('исходный массив: ')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
for i in range(n):
    for j in range(m):
        minn=min(a[i])
        x=a[i].index(min(a[i]))
    tmin=a[i][0]
    a[i][0]=a[i][x]
    a[i][x]=tmin
for i in range(n):
    for j in range(m):
        maxx=max(a[i])
        y=a[i].index(max(a[i]))
    tmax=a[i][m-1]
    a[i][m-1]=a[i][y]
    a[i][y]=tmax
print('новый массив: ')
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()