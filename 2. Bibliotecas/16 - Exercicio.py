#Desafio 16 - crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: digete um número: 6.127. O numero 6.127 tem a parte inteira 6 DICA: biblioteca math

from math import trunc

num = float(input("Digite um Numero Real: "))

print("o numero inteiro é: {}".format(trunc(num)))