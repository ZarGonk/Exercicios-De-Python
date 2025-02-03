# Desafio 59 - Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Digite um numero: '))
c = num
fat = 1

while c > 0:
  print('{}'.format(c),end='')
  print(' x ' if c > 1 else ' = ', end='')
  fat = c * fat
  c = c - 1
print('{} \n\n OU'.format(fat))
print('\n{}! = {}'.format(num, fat))
