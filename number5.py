import csv


'''
функция хэширования
'''
def hash(s):
    alp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890:-'
    m = 10**9 + 9
    p = 65
    d = {}
    for ind, symbol in enumerate(alp, 1):
        d[symbol] = ind

    r = 0
    for i in range(len(s)):
        r += int(d[s[1]])*(p**i)
    return str(r % m)

'''
Считывание файла в двумерный массив
'''
f = open('game.txt', encoding = 'utf-8')
data=[x.strip().split('$') for x in f]
f.close()

list = []

for i in range(1, len(data)):
    s = data[i][0]+data[i][1]
    s = hash(s)
    list.append([s, data[i][0], data[i][2]])


'''
Создание нового scv файла
'''
with open('game_with_hash.csv', 'w', encoding = 'utf-8') as file:
    w = csv.writer(file)
    w.writerows(['hash', 'GameName', 'characters'])
    w.writerows(list)
