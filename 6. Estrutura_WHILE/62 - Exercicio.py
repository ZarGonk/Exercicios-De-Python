# Desafio 62 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#num = int(input('Digite um numero inteiro: '))
print('    Sequencia de Fibonacci')
print('-='*15)
  
num = int(input("Quantos Numeros Deseja Mostrar: "))
t1 = 0
t2 = 1

c = 3
print('{} -> {}'.format(t1, t2), end='')
while c <= num:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print(' \nfim')