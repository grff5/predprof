'''
Считывание файл в двумерный массив
'''
f = open('game.txt', encoding = 'utf-8')
data=[x.strip().split('$') for x in f]
f.close()

'''
Ввод и поиск персонажа в играх 
'''
x=input()
while x!='game':
    c=0
    for i in range(1, len(data)):
        if x==data[i][1]:
            c+=1
            if c==1:
                print(f'Персонаж {x} встречается в играх:')
                print(data[i][0])
            if c>1 and c<5:
                print(data[i][0])
            if c==5:
                print(data[i][0])
                print('и др.')
                break
    if c==0: print('Этого персонажа не существует')
    x=input()