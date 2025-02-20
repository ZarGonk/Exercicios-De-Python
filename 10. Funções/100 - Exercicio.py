# Exercício 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#   A primeira função vai sortear 5 números e colocá-los dentro da lista.
#   A segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
    print('Sortedo 5 valores: ',end='')
    for i in range(0, 5):
        num = randint(0, 10)
        numeros.append(num)
        print(num, end=' ', flush=True)
        sleep(.5)
    print()

def somaPar(lista):
    s = 0
    for num in numeros:
        if num % 2 == 0:
            s += num
    print(f'A soma dos pares entre {numeros}: {s}')


#Codigo principal
numeros = []
sorteia(numeros)
somaPar(numeros)

