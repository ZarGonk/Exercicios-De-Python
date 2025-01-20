# Desafio 24 - crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

n = str(input("Digite o nome da sua cidade: ")).strip()
min = n.lower()

print(min[:5] == "santo")