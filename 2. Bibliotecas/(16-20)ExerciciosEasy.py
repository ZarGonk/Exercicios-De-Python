#Desafio 16 - crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: digete um número: 6.127. O numero 6.127 tem a parte inteira 6 DICA: biblioteca math

from math import trunc

num = float(input("Digite um Numero Real: "))

print("o numero inteiro é: {}".format(trunc(num)))'''
'''



#Desafio 19 - um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
'''import random

n1 = input("informe nome do 1° aluno: ")
n2 = input("informe nome do 2° aluno: ")
n3 = input("informe nome do 3° aluno: ")
n4 = input("informe nome do 4° aluno: ")
lista = [n1, n2, n3 ,n4]
escolhido = random.choice(lista)

print("{}".format(escolhido))'''

#Desafio 20 - o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
'''
from random import sample

a1 = input("informe nome do 1° aluno:")
a2 = input("informe nome do 2° aluno:")
a3 = input("informe nome do 3° aluno:")
a4 = input("informe nome do 4° aluno:")
lista = [a1, a2, a3, a4]
escolhido = sample(lista, k=4)

print("a ordem de apresentação sera \n{}".format(escolhido))
'''