# Exercício 87: Aprimore o exercício anterior, mostrando no final:
#   A soma de todos os valores pares digitados.
#   A soma dos valores da terceira coluna.
#   O maior valor da segunda linha.

matriz = []
pares = soma = maior = 0
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
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
             maior = matriz[l][c]
    print()
print(f'The pairs added together: {pares}')
print(f'Largest value of the third column: {soma}')
print(f'Highest value of the segund line: {maior}')