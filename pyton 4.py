import math

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
d = float(input("Введите значение d: "))

otvet = math.isclose(a * d, b * c)
print(otvet)
