import os


while True:
    file = open('tasks.txt','r',encoding='UTF-8').read().split('|')
    for i in file:
        if i.endswith('.exe'):
            os.system('taskkill /f /im {}'.format(i))
            print(i+' terminated was successfully')