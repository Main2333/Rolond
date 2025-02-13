import math

x = float(input("Ведите координату x: "))
y = float(input("Введите координату y: "))

x1, y1, x2, y2 = 1, 1, 4, 4

a, b, c = 5, 5, 3

i = x1 <= x <= x2 and y1 <= y <= y2

wer = (x - a) ** 2 + (y - b) ** 2
rew = wer <= c ** 2

if i or rew:
    print(True)
else:
    print(False)
