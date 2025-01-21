# Desafio 33 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))
c = float(input('Digite terceiro numero: '))

#Verifica o Menor
menor =  a
if (b < a) and (b < c):
  menor = b
if (c < a) and (c < b):
  menor = c

#Verifica o Maior
maior = a
if (b > a) and (b > c):
  maior = b
if (c > a) and (c > b):
  maior = c

print("O maior número é {}".format(maior))
print('O menor numero é {}'.format(menor))