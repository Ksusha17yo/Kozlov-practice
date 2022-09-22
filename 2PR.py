import math

a = float(input("¬ведите x "))
b = float(input("¬ведите y "))
c = float(input("¬ведите z "))
d = (math.pow((b + (math.pow((a - 1), 1./3))), 1./4))/(math.fabs(a - b) * (math.pow(math.sin(c), 2) + math.tan(c)))
print("s= {0:.6f}".format(d))