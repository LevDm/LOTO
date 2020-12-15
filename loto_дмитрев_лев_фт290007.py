# -*- coding: utf-8 -*-
import random


def OTVET(): #запрос дейсвия
    i = True
    while i == True:
        print('\n-----')
        otvet = input('* Действие: ')
            
        if  otvet.isdigit() == True:
            otvet = int(otvet)
            if 0 <= otvet <= 1: break
            else:
                print('\n** Число не попадает в диапазон действий!')
                continue
        else:
            print('\n** Необходимо целое число!')
            continue
    print('\n-----')
    return otvet


def GO_LOTO():
    i = True
    while i == True:
        print('\n-----')
        number = input('* Количесво чисел: ')            
        if  number.isdigit() == True:
            number = int(number)
            break
        else:
            print('\n** Необходимо целое число!')
            continue
    print('\n-----')
    
    sloti = []
    
    for n in range(number+1): 
        if n != 0: sloti.append(n)
    
    for w in range(len(sloti)):
        
        print('\nЧтобы получить число жми клавишу ЭНТЕР')
        while i == True:
            enter = input('-')
            if enter == '': break
            else: print('Это не энтер')
            
        X = 'x'
        while X == 'x': X = random.choice(sloti)
        
        print('ВЫПАЛО:',str(X))
        
        for q in range(len(sloti)):
            if sloti[q] == X: sloti[q] = 'x'
            
        print('\n',sloti)
        print('\n-----')
    
    

go = True
while go == True: 
    GO_LOTO() 
    print('0-выход/n1-повтор')
    if OTVET() == 0: break 
    


