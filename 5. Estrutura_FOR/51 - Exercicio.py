# Desafio 51 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.
num = int(input('Informe o primerio termo: '))
pa = int(input('Qual a Razao: '))

print('\nOs 10 pimeiros termos são:\n')
for i in range(1 , 11):
  an = num + (i - 1) * pa
  print(an, end=' -> ')
print('ACABOU')
