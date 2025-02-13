import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
h = float(input("Введите шаг h: "))

print("{:>10} {:>10}".format("x", "F(x)"))
print("-" * 20)

x = a
while x <= b:
    F_x = x - math.sin(x)
    print("{:>10.4f} {:>10.4f}".format(x, F_x))
    x += h
if x > b and abs(x - b) > 1e-9:  
    F_x = b - math.sin(b)
    print("{:>10.4f} {:>10.4f}".format(b, F_x))
