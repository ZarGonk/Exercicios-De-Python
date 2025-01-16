#Desafio 19 - um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random

n1 = input("informe nome do 1° aluno: ")
n2 = input("informe nome do 2° aluno: ")
n3 = input("informe nome do 3° aluno: ")
n4 = input("informe nome do 4° aluno: ")

lista = [n1, n2, n3 ,n4]
escolhido = random.choice(lista)

print("{}".format(escolhido))