# Exercício 95: Aprimore o exercício 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

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