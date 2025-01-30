# Desafio 52 - Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite Um Numero Inteiro: '))

if num <= 1:
  print('Esse não e primo!')
elif num == 2 or num == 3:
  print('Ele é Primo !!!')
elif num % 2 == 0 or num % 3 == 0:
  print('O {} não e primo!'.format(num))
else:
  print('Esse numero é primo: {}'.format(num))
