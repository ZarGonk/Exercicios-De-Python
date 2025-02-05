#Exercício 90: Faça um programa que leia nome e média de um aluno, 
# guardando também a situação em um dicionário. No final, mostre o 
# conteúdo da estrutura na tela.
'''aluno = dict()

aluno['Nome'] = str(input('Nome: ')).strip().capitalize()
aluno['Media']= float(input(f'Media do {aluno['Nome']}: '))

if aluno["Media"] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print()
print(f'{"Boletim":=^30}')
print(f'O nome é: {aluno["Nome"]}')
print(f'A media é: {aluno["Media"]}')
print(f'Situação do aluno: {aluno['Situação']}')

print()
print(f'{"Boletim":=^30}')
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')'''

#Exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham 
# resultados aleatórios. Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor 
# tirou o maior número no dado.
'''from random import randint
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
'''
#Exercício 92: Crie um programa que leia nome, ano de nascimento e 
# carteira de trabalho e cadastre-os (com idade) em um dicionário. 
# Se, por acaso, a CTPS for diferente de 0, o dicionário receberá 
# também o ano de contratação e o salário. Calcule e acrescente, 
# além da idade, com quantos anos a pessoa vai se aposentar.
'''from datetime import datetime
dados = dict()

#dados caso nao tenha carteira de trabalho
dados['Nome'] = str(input('Nome: '))

ano = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
dados['Idade'] = ano_atual - ano

#dados caso haja carteira de trabalho
dados['Carteira'] = int(input('Carteira de trabalho(0 - nao tem): '))
if dados['Carteira'] != 0:
    dados['Ano De Contrataçao'] = int(input('Ano de contrataçao: '))
    dados['Salario'] = float(input('Salario: '))

    #aposentadoria
    dados['Aposentadoria'] = (dados['Ano De Contrataçao'] - ano) + 35
#Gera os dados cadastrados
print(f'\n=-=-=-=-Dados De {dados["Nome"]}-=-=-=-=')
for c, v in dados.items():
    print(f'{c}: {v}')'''

#Exercício 93: Crie um programa que gerencie o aproveitamento de um 
# jogador de futebol. O programa vai ler o nome do jogador e quantas 
# partidas ele jogou. Depois, vai ler a quantidade de gols feitos em 
# cada partida e, no final, tudo isso será guardado em um dicionário, 
# incluindo o total de gols feitos durante o campeonato.
'''futebol = dict()
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
    print(f'=> Na partida {i+1}, fez {g} gols')'''

#Exercício 94: Crie um programa que leia nome, sexo e idade de várias 
# pessoas, guardando os dados de cada pessoa em um dicionário e todos os
# dicionários em uma lista. No final, mostre:
#   Quantas pessoas foram cadastradas.
#   A média de idade do grupo.
#   Uma lista com todas as mulheres.
#   Uma lista com todas as pessoas com idade acima da média.
'''pessoas = list()
woman = list()
sup_idade = list()
dados = dict()
tot_idade = 0

while True:
    #Cadastra De Pessoas
    dados['Nome']  = str(input('Nome: ')).strip().capitalize()
    while True:
        dados['Sexo']  = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if dados['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    print()

    #Para o loop
    while True:
        op = str(input('Deseja parar[S/N]? ')).strip().upper()
        if op in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if op == 'S':
        break

#Media de idade:
for p in pessoas:
    tot_idade += p['idade']
    if p['Sexo'] == 'F':
        woman.append(p['Nome'])
media = tot_idade / len(pessoas)

for p in pessoas:
    if p['idade'] > media:
        sup_idade.append(p['Nome'])

print()
print('-=-'*15)
print(f'Total de pessoas cadastradas {len(pessoas)}')
print(f'A media de idades é {media:.2f}')
if len(woman) > 0:
    print(f'Mulheres Registradas {woman}')
else:
    print('Não teve mulheres registradas')

if len(sup_idade) > 0:
    print(f'Pessoas com a idade acima da media {sup_idade}')
print('-=-'*15)'''

#Exercício 95: Aprimore o exercício 93 para que ele funcione com vários 
# jogadores, incluindo um sistema de visualização de detalhes do 
# aproveitamento de cada jogador.
futebol = []
jogadores = {}

while True:
    jogadores['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas Jogadas: '))
    gols = list()
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i+1}: ')))
    jogadores['Gols'] = gols[:]
    jogadores['Total'] = sum(gols)
    futebol.append(jogadores.copy())

    # Opção para encerrar cadastro
    while True:
        stop = str(input('Deseja parar[S/N]: ')).strip().upper()[0]
        if stop in 'SN':
            break
        print('ERRO! Opção Invalidade')
    if stop == 'S':
        break
    print()

print('-=-=-=-=-=-=-=TABELA=-=-=-=-=-=-=-')
print(f'{"Cod.":<5}{"Nome":<10}{"Gols":<10}{"Total"}')
print('-'*32)
for i, p in enumerate(futebol):
    gols_str = ','.join(map(str, p['Gols']))
    print(f'{i:<5}{p["Nome"]:<10}{gols_str:<10}{p["Total"]}')
print('-'*30)


while True:
    print()
    aprov = int(input('Deseja ver o aproveitamento de qual jogador ?'))
    if aprov == 999:
        break

    if 0 <= aprov < len(futebol):
        jogador = futebol[aprov]
        print(f'Detalhes do jogador {jogador["Nome"]}: ')
        for i, gols in enumerate(jogador['Gols']):
            print(f'Partida {i+1}: {gols} gols')
    else:
        print('Jogador nao encontrado')