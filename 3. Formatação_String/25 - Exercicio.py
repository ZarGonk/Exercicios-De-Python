# Desafio 25 - crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input("Digite o nome da pessoa: "))

print("No nome {} tem foi encontrado Silva ? {}".format(name, "SILVA" in name.upper())) 