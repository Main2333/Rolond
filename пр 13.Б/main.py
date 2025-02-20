def wer(rew):
    try:
        mas = []
        with open(rew, 'r', encoding='utf-8') as n:
            for i in n:
                mas.extend(map(float, i.split()))
        if mas:
            minimum = min(mas)
            print("Минимальное число в файле: {}".format(minimum))
        else:
            print("Файл не содержит вещественных чисел.")

    except FileNotFoundError:
        print("Ошибка: файл '{}' не найден.".format(rew))
    except ValueError:
        print("Ошибка: файл содержит недопустимые данные.")
    except Exception as e:
        print("Произошла ошибка: {}".format(e))

file = 'numbers.txt' 
wer(file)
