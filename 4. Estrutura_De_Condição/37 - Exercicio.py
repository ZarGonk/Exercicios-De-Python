# Desafio 37 - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite Um Valor: '))
print('\nQual Base numerica deseja tratar:\n\n1 para binário\n2 para octal\n3 para hexadecimal')

converter = int(input('\nQual Sua Base? '))
#Converte Para Binario
if converter == 1:
  binario = bin(num)
  print('\nA conversão de {} para binario é {}'.format(num, binario[2:]))
#Converte Para Octal
elif converter == 2:
  octal = oct(num)
  print('\nA conversão de {} para binario é {}'.format(num, octal[2:]))
#Converte Para Hexadecimal
elif converter == 3:
  hexadecimal = hex(num)
  print('\nA conversão de {} para binario é {}'.format(num, hexadecimal[2:]))
else:
  print('\nVoce nao escolheu uma base existente')
