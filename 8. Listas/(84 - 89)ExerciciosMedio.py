#Exercício 84: Faça um programa que leia nome e peso de várias pessoas, 
#guardando tudo em uma lista. No final, mostre:
#   Quantas pessoas foram cadastradas.
#   Uma listagem com as pessoas mais pesadas.
#   Uma listagem com as pessoas mais leves.
'''dados   = list()
pessoas = list()
maior = menor = 0

while True:
    dados.append(str(input('Enter your name: ')))
    dados.append(float(input('Enter your weight: ')))

    pessoas.append(dados [:])
    dados.clear()

    stop = str(input('Want to stop[Y/N]: ')).strip().upper()
    if stop == 'Y':
         break

maior = menor = pessoas[0][1]

for p in pessoas:
    if p[1] > maior:
          maior = p[1]
    if p[1] < menor:
         menor = p[1]

print(f'Total number of registered people was: {len(pessoas)}')
print(f'The bigger weight registered was: {maior} of people: ',end='')
for p in pessoas:
     if maior == p[1]:
          print(p[0],end='...')
print(f'\nThe minor weight registered was: {menor} of people: ',end='')
for p in pessoas:
     if menor == p[1]:
          print(p[0],end='...')'''

#Exercício 85: Crie um programa onde o usuário possa digitar sete valores 
#numéricos e cadastre-os em uma lista única que mantenha separados os 
#valores pares e ímpares. No final, mostre os valores pares e ímpares em 
#ordem crescente.
'''number = [[], []]
for i in range(7):
    num = int(input('Enter a number: '))

    if num % 2 == 0:
        number[0].append(num)
    else:
        number[1].append(num)
number[0].sort()
number[1].sort()

print(f'The even values entered were: {number[0]}')
print(f'The odd entered were: {number[1]}')'''

#Exercício 86: Crie um programa que crie uma matriz de dimensão 3x3 e 
#preencha com valores lidos pelo teclado. No final, mostre a matriz na 
#tela, com a formatação correta.
'''matriz = []
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
    print()'''

#Exercício 87: Aprimore o exercício anterior, mostrando no final:
#   A soma de todos os valores pares digitados.
#   A soma dos valores da terceira coluna.
#   O maior valor da segunda linha.

'''matriz = []
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
print(f'Highest value of the segund line: {maior}')'''
#Exercício 88: Faça um programa que ajude um jogador da Mega Sena a criar 
#palpites. O programa vai perguntar quantos jogos serão gerados e vai 
#sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma 
#lista composta.
'''from random import sample
print('Mega Sena'.center(30))
print('-=-'*10)

num = int(input('Want to play you want to: '))
print(f'-=-=-= Sorteados {num} Jogos =-=-=-')
for i in range(0, num):
    sorteados = sample(range(1, 61), 6)
    print(f'{i+1}° Jogo: {sorteados}')
print(f"{' < Good Game > ':=^34}")'''

#'''Exercício 89: Crie um programa que leia nome e duas notas de vários 
#alunos e guarde tudo em uma lista composta. No final, mostre um boletim 
#contendo a média de cada um e permita que o usuário possa mostrar as 
#notas de cada aluno individualmente.
boletim = []
while True:
    nome = str(input('Enter the name: '))
    n1 = float(input('Enter the first note: '))
    n2 = float(input('Enter the second note: '))

    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])

    # Pergunta se quer continuar, caso contrário, para
    stop = ''
    while stop not in ('Y', 'N'):
        stop = str(input('Want to stop [Y/N]: ')).strip().upper()
        if stop == 'N':
            break
    if stop == 'Y':
        break

# Exibindo o boletim com a média de cada aluno
print('\n')
print(f"{'BOLETIM':=^30}")
print(f"{'N°.':<4} {'Nome':<15} {'Média':>7}")
print('-=' * 15)
for i, a in enumerate(boletim):
    print(f'{i + 1:<4} {a[0]:<15} {a[2]:>7.2f}')

# Mostra as notas de um aluno específico
while True:
    opcao = int(input('Do you want to see which student\'s grade (999 stops): '))
    if opcao == 999:
        print("Finalizando...")
        break
    if 0 <= opcao - 1 < len(boletim):
        print(f'Notas de {boletim[opcao - 1][0]} são {boletim[opcao - 1][1]}')
    else:
        print("Aluno não encontrado.")
