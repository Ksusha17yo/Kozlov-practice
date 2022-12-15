with open('Козлов_С.А._УБ-22_vvod.txt', 'r', encoding='utf-8-sig') as f:
    line=f.readlines()
    matrix=[element.replace("\n", "").split() for element in line]
    print('матрица')
    print(matrix)
n=len(matrix)
m=len(matrix[0])
a=matrix
s=0
kp=0
for i in range(n):
    for j in range(n):
        if j>i:
            s+=int(a[i][j])
            if int(a[i][j])>0:
                kp=kp+1
print('сумма элементов над главной диагональю: ', s)
print('их количество: ', kp)
with open('Козлов_С.А._УБ-22_vivod1.txt', 'a+', encoding='utf-8-sig') as f:
    f.write('сумма элементов над главной диагональю: ')
    f.write(str(s))
    f.write('\n')
    f.write('их количество: ')
    f.write(str(kp))
    f.write('\n')
