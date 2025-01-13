#Desafio 10 - Crie um programa que faça a taboada de 1 numero
n = int(input("Qual taboada você deseja: "))
um = n * 1
dois = n * 2
tres = n * 3
quatro = n * 4
cinco = n * 5
seis = n * 6
sete = n * 7
oito = n * 8 
nove = n * 9
dez = n * 10

print()
print("=====Taboada=====")
print("1 * {} = {} \n2 * {} = {}\n3 * {} = {}\n4 * {} = {}\n5 * {} = {}".format(n, um, n, dois, n, tres, n, quatro, n, cinco))
print("6 * {} = {} \n7 * {} = {}\n8 * {} = {}\n9 * {} = {}\n10 * {} = {}".format(n,seis, n, sete, n, oito, n, nove, n, dez))