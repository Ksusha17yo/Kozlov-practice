import math

a = float(input("������� x "))
b = float(input("������� y "))
c = float(input("������� z "))
d = (math.pow((b + (math.pow((a - 1), 1./3))), 1./4))/(math.fabs(a - b) * (math.pow(math.sin(c), 2) + math.tan(c)))
print("s= {0:.6f}".format(d))