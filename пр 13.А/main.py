def wer(rew):
    try:
        with open(rew, 'r', encoding='utf-8') as n:
            test = n.read()
        dokumen = test.split()
        con = 0
        for i in dokumen:
            clen = ''.join(har for har in i if har.isalpha()).lower()
            if len(clen) > 0 and clen[0] == clen[-1]:
                con += 1

        print("Количество слов, начинающихся и заканчивающихся на одну и ту же букву: {}".format(con))

    except FileNotFoundError:
        print("Ошибка: файл '{}' не найден.".format(rew))
    except Exception as e:
        print("Произошла ошибка: {}".format(e))

file = 'input.txt' 

wer(file)
