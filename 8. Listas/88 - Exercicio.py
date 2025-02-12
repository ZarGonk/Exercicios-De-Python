# Exercício 88: Faça um programa que ajude um jogador da Mega Sena a criar 
#palpites. O programa vai perguntar quantos jogos serão gerados e vai 
#sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma 
#lista composta.
from random import sample
print('Mega Sena'.center(30))
print('-=-'*10)

num = int(input('Want to play you want to: '))
print(f'-=-=-= Sorteados {num} Jogos =-=-=-')

for i in range(0, num):
    sorteados = sample(range(1, 61), 6)
    print(f'{i+1}° Jogo: {sorteados}')
print(f"{' < Good Game > ':=^34}")
