# Desafio 53 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. 
# Exemplos: APOS A SOPA, A SACADA DA CASA, 
# A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Qual Sua Frase: ')).upper()
frasejunta = frase.replace(' ','')

if frasejunta == frasejunta[::-1]:
  print('\nA frase é um Palindromo')
else:
  print('\nA frase não é um Palindromo')
print('\nO inverso da frase é: \n{}'.format(frasejunta[::-1]))
