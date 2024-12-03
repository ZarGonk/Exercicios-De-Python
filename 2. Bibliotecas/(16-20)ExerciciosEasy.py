#Desafio 16 - crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: digete um número: 6.127. O numero 6.127 tem a parte inteira 6 DICA: biblioteca math
'''
from math import trunc

num = float(input("Digite um Numero Real: "))

print("o numero inteiro é: {}".format(trunc(num)))'''

#Desafio 17 - faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
'''
from math import hypot

v1 = float(input("Diga seu A: "))
v2 = float(input("Diga seu B: "))
hip = hypot(v1, v2)

print("o Valor da sua Hipotenisa é: {:.2f}".format(hip))'''

#Desafio 18 - faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
'''import math

ang = float(input("Informe o angulo: "))
ang_rad = math.radians(ang)

coss = math.cos(ang_rad)
sen = math.sin(ang_rad)
tang = math.tan(ang_rad)

print("Do seu angulo {} aqui esta:\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}".format(ang, coss, sen, tang))'''

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