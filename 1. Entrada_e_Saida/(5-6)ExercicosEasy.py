#Desafio 5 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''
x = input("Digite algo: ")
print("o tipo primitivo é:", type(x))
print("é numerico ?", x.isnumeric())
print("é um alfabeto", x.isalpha())
print("é um numero", x.isalnum())
print("é um espaço", x.isspace())
'''

#Desafio 6 - Faça uma Programa que leia dois numeros e mostre a soma

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

op = v1 + v2 

print("Conta: {} + {} = {} ".format(v1, v2, op))

