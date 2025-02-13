import math

E = float(input("Введите значение E: "))
a = [1]  
n = 1

while True:
    wer = 0.5 * (a[n-1] + 2 / a[n-1])
    a.append(wer)
    n += 1

    if abs(a[n-1]**2 - 2) < E:
        break
print("Наименьший номер n:", n)
print("Элементы последовательности:")
for i in range(1, n+1):
    print("a_{} = {:.6f}".format(i, a[i-1]))
