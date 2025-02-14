# Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

players = dict()
rank = list()
#Sorteia um dado e add o dado e o player ao dicionario "players"
players['Player1'] = randint(1, 6)
players['Player2'] = randint(1, 6)
players['Player3'] = randint(1, 6)
players['Player4'] = randint(1, 6)

#Mostra os dados sorteado por cada player
print(f'{"Dados Sorteados":=^30}')
for key, value in players.items():
    print(f'O {key} tirou {value}')
    sleep(1)
print('-=-'*15)

#Mostra em ordem do maior numero o placar dos jogadores
rank = sorted(players.items(), key=itemgetter(1), reverse=True)
print('===Ranking dos jogadores===')
for i, player in enumerate(rank):
    print(f'{i+1}° Lugar: {player[0]} com {player[1]}')
    sleep(1)

