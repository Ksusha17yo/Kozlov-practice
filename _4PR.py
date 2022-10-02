x = input("Введите строчку с точкой ")
y = 0

for i in range(len(x)):
    if x[i] == " ":
        y += 1
print("В этой строке", y+1, "слов")
