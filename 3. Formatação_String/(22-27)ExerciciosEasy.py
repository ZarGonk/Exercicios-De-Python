#Desafio 22 - crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiusculas e minusculas, quantas letras ao todo (sem considerar espaços), quantas letras tem o primeiro nome.
'''
nome = str(input("Qual é o seu nome: ")).strip()
M = nome.upper() #maiuscula
m = nome.lower() #minuscula
space = nome.split() #Divide string
uni = "".join(space) #Uni string
primeiro_nome = len(nome.split()[0])  # Pega o primeiro nome

print("Nome Maiusculo:{} \nNome Minusculos: {}\nSem Espaço: {}\nQuantidade de letras no primeiro nome: {}".format(M, m, len(uni), primeiro_nome))
'''






