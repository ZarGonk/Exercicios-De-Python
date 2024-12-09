#Desafio 46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''from time import sleep
for i in range(10, -1, -1):
  print('{} ...'.format(i))
  sleep(0.5)
print('\nOLHA EXLOSÂO\nQUANDO ELA BATE COM A BUNDA NO CHÃO')
'''
#Desafio 47 - crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
'''for i in range(0, 51, 2):
  print(i, end=' ')'''

#Desafio 48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''s = 0
for i in range(1, 501):
  if i % 2 != 0 and i % 3 == 0:
    s = s + i

print('A Soma dentre os impares,multiplos de 3 é: {}'.format(s))

#OUUU

"""S = 0
for i in range(1, 500, 2):
    if (i%3) == 0 :
        S += i
print(S)"""

'''
#Desafio 49 - Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''
num = int(input('Qual Tabuada Voce Deseja: '))
for i in range(0, 11):
  tabuada = i * num
  print('{} x {} = {}'.format(i, num, tabuada))
'''
#Desafio 50 - Desenvolva um programa que leia seis números e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.
'''s = 0
for i in range(0,6):
  num = int(input('Digite Um Numeros Inteiros: '))
  if num % 2 == 0:
    s += num
print('A soma dos Pares é: {}'.format(s))'''