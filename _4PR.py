x = input("������� ������� � ������ ")
y = 0

for i in range(len(x)):
    if x[i] == " ":
        y += 1
print("� ���� ������", y+1, "����")
