#Desafio 20 - o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import sample

a1 = input("informe nome do 1° aluno:")
a2 = input("informe nome do 2° aluno:")
a3 = input("informe nome do 3° aluno:")
a4 = input("informe nome do 4° aluno:")
lista = [a1, a2, a3, a4]
escolhido = sample(lista, k=4)

print("a ordem de apresentação sera \n{}".format(escolhido)) 