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
#Desafio 23 - faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. ex: unidade: 4 dezena: 3 centena: 8 milhar: 1
'''
n = int(input("Digite um número entre 0 e 9999: "))

# Extrai os dígitos individualmente
u = (n // 1) % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = (n // 1000) % 10

# Exibe os dígitos separadamente
print("Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}".format(m, 
c, d, u))'''

#Desafio 24 - crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''
n = str(input("Digite o nome da sua cidade: ")).strip()
min = n.lower()

print(min[:5] == "santo")
'''
#Desafio 25 - crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
name = str(input("Digite o nome da pessoa: "))

print("No nome {} tem foi encontrado Silva ? {}".format(name, "SILVA" in name.upper()))
'''
#Desafio 26 - faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a ultima vez.
'''
f = str(input("digite sua frase: ")).strip()
min = f.lower()


print("Quantos (A) tem: {}\nPrimeira posicao: {}\nUltima posicao: {}".format(min.count("a"), min.find("a"), min.rfind("a")) )
'''
#Desafio 27 - faça um programa que leia o nome completo de uma pessoa e mostre: o primeiro e o ultimo nome separadamente. Ex.: Ana Maria de Souza. Prinome: Ana Sobrenome: Souza

name = str(input("Digite seu nome completo: ")).strip()

c = name.split() #Separa o nome
p = c[0] #primeiro nome
u = c[-1] #ultimo nome

print("Primeiro nome : {}\nUltimo nome: {}".format(p, u))


