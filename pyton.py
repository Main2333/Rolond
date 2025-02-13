import math
a = int(input('Введите значения переменой: a: '))
x = int(input('Введите значения переменой: x: '))
y = int(input('Введите значения переменой: y: '))
f = pow((x + a * y), 3) + 1
d = a + abs(x - y - pow(a, 3))
w = pow(a, 2) + pow(x, 3)
q = pow(y, 3) - a
wer = (f / d) + (w / q)
print(wer)