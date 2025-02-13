import math
a = 5
b = 6
c = 7

f = (a + b + c) / 2

rew = math.sqrt(f * (f - a) * (f - b) * (f - c))

r = rew / f

go = math.pi * r ** 2

print('Значения a: ' + str(a), 'Значения b: ' + str(b), 'Значения c: ' + str(c))
print("Площадь круга: {:.2f}".format(go))
