# Desafio 27 - faça um programa que leia o nome completo de uma pessoa e mostre: o primeiro e o ultimo nome separadamente. Ex.: Ana Maria de Souza. Prinome: Ana Sobrenome: Souza

name = str(input("Digite seu nome completo: ")).strip()

c = name.split() #Separa o nome
p = c[0] #primeiro nome
u = c[-1] #ultimo nome

print("Primeiro nome : {}\nUltimo nome: {}".format(p, u))
