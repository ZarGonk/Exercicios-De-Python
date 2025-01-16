#Desafio 13 - Crie um programa que leio o preço do produto, e mostre seu novo preço de 5% de desconto
'''
v = float(input("qual é o valor desatualizado do produto? "))

desconto = v * 0.05
preco = v - desconto

print("O valor atualizado do produto é: {:.2f}".format(preco))
'''
#Desafio 15 - Faça a media aritmetica da nota de 1 aluno 
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2

print("A media aritmetica entre {} e {} é igual a {:.2f}".format(n1, n2, media))
