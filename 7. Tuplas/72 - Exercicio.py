# Exercício 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um numero: '))

if 0 <= num <= 20:
    print(f'O numero {num} por extenso fica {numero[num]}')
else:
    print(f'Numero {num} nao encontrado')