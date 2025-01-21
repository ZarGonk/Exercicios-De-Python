#Desafio 35 - Desenvolva um programa que leia o comprimento de tres retas e diga ao usuário se elas podem ou não formar um triângulo

a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))
c = float(input('Digite terceiro numero: '))

if a < b + c and b < a + c and c < a + b:
  print('\nPode formar um tringulo')
else:
  print('\nNao forma um triangulo')
