# Exercício 86: Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = []
#Faz a matriz e armazena os resultados
for l in range(3):
    linha = []
    for c in range(3):
        linha.append(int(input(f'Enter number [{l}][{c}]: ')))
    matriz.append(linha) 
#Imprime a matriz
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()