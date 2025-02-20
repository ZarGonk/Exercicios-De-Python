# Exercício 99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep

def maior(*num):

    print('Analisando os valores passados...')
    if len(num) > 0:
        for i in num:
            print(i, end=" ", flush=True)
            sleep(.5)
        print(f'Foram informados {len(num)} valores ao todo')
        print(f'O maior numero foi: {max(num)}')
        print('-=-'*10)
        
    else:
        print('Não foram informados valores')
        print('Maior valor foi 0')

#Codigo principal
maior(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
maior(randint(1,10), randint(1,10), randint(1,10))
maior(randint(1,10), randint(1,10))
maior(randint(1,10))
maior()