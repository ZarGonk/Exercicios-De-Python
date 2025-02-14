# Exercício 93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois, vai ler a quantidade de gols feitos em cada partida e, no final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

futebol = dict()
gols = list()

futebol['Nome'] = str(input('Nome do jogador: '))

partidas = int(input('Quantas partidas Jogadas: '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {i+1}: ')))

futebol['Gols'] = gols[:]
futebol['Total'] = sum(gols)

print('-=-'*15)
print(futebol)
print('-=-'*15)
for c, v in futebol.items():
    print(f'A chave {c} tem o valor {v}')
print('-=-'*15)
print(f'O jogador {futebol['Nome']} jogou {len(gols)} partidas')
for i, g in enumerate(gols):
    print(f'=> Na partida {i+1}, fez {g} gols')

