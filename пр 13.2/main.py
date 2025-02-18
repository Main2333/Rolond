import os

def wer(filename):
    c = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for i in file:
                part = i.strip().split()
                if len(part) == 2:
                    a = int(part[0])
                    b = float(part[1])
                    c.append((a, b))
    except FileNotFoundError:
        print("Ошибка: файл {} не найден.".format(filename))
        return []
    except Exception as e:
        print("Ошибка при чтении файла: {}".format(e))
        return []
    return c

def analyze_c(c, t):
    if not c:
        return [], 0, 0, False

    total1 = sum(a for a, _ in c)
    total_b = sum(b for _, b in c)
    over = total_b / total1 if total1 > 0 else 0
    
    # а) Багаж, средняя масса одной вещи в котором отличается не более чем на t кг
    suit = [b for b in c if abs((b[1] / b[0]) - over) <= t]
    
    # б) Число пассажиров, имеющих более двух вещей, и число пассажиров с вещами больше среднего
    more = sum(1 for a, _ in c if a > 2)
    avg = total1 / len(c) if c else 0
    than = sum(1 for a, _ in c if a > avg)
    
    # в) Имеется ли пассажир с одной вещью менее t кг
    sing = any(a == 1 and b < t for a, b in c)
    
    return suit, more, than, sing

filename = "Bagazh.txt"
if not os.path.exists(filename):
    print("Ошибка: файл {} не найден.".format(filename))
else:
    try:
        t = float(input("Введите значение t: "))
        c = wer(filename)

        suit, two, than, has = analyze_c(c, t)

        # Вывод результатов
        print("Багаж с подходящей средней массой вещи:", suit)
        print("Число пассажиров с более чем 2 вещами:", two)
        print("Число пассажиров с вещами больше среднего:", than)
        print("Есть ли пассажир с одной вещью менее t кг:", "Да" if has else "Нет")
    except ValueError:
        print("Ошибка: введите корректное число для t.")
