# Exercício 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
for i in range(5):
    numeros.append(int(input(f'Digite {i+1}° valor: ')))

maior = max(numeros)
menor = min(numeros)

# Encontrando as posiçoes do menor valor
posicoes_maior = []
for i, num in enumerate(numeros):
    if num == maior:
        posicoes_maior.append(i + 1)

# Encontrando as posições do menor valor
posicoes_menor = []
for i, num in enumerate(numeros):
    if num == menor:
        posicoes_menor.append(i + 1)

print(f'O maior valor add foi: {maior} na posição {posicoes_maior}°')
print(f'O menor valor add foi: {menor} na posição {posicoes_menor}°')