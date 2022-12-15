with open('D:\Козлов_С.А._УБ-22_vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print('матрица')
    print(matrix)
n=len(matrix)
m=len(matrix[0])
a=matrix
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
with open('D:\Козлов_С.А._УБ-22_vivod2.txt', 'w', encoding='utf-8-sig') as f:
    f.write(str(a))