# Desafio 23 - faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados. ex: unidade: 4 dezena: 3 centena: 8 milhar: 1

n = int(input("Digite um número entre 0 e 9999: "))

# Extrai os dígitos individualmente
u = (n // 1) % 10
d = (n // 10) % 10
c = (n // 100) % 10
m = (n // 1000) % 10

# Exibe os dígitos separadamente
print("Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}".format(m, 
c, d, u)) 
