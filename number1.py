import csv 
'''
Считывание файл в двумерный массив
'''
f = open('game.txt', encoding = 'utf-8')
data=[x.strip().split('$') for x in f]
f.close()
'''
Отчёт по играм и исправление представленной информации
'''
for i in range(1, len(data)):
    if '55' in data[i][2]:
        print(f'У персонажа {data[i][1]} в игре {data[i][0]} нашлась ошибка с кодом {data[i][2]}. Дата фиксации: {data[i][3]}')
        data[i][3] = '0000-00-00'
        data[i][2] = 'Done'

'''
Создание нового scv файла
'''
with open('game_new.csv', 'w', encoding = 'utf-8') as file:
    w = csv.writer(file)
    w.writerows(['GameName', 'characters', 'nameError', 'date'])
    w.writerows(data)
