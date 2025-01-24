# esafio 38 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: - O primeiro valor é maior - O segundo valor é maior - Não existe valor maior,os dois são iguais.

num1 = int(input('Digite o primeiro Numero: '))
num2 = int(input('Digite o segundo Numero: '))

if (num1 > num2):
  print('Numero {} é Maior que {}'.format(num1, num2))
elif(num2 > num1):
  print('Numero {} é Maior que {}'.format(num2, num1))
elif (num1 == num2):
  print('\n\033[0;31mOs Dois Numeros Tem Valores Iguais')
