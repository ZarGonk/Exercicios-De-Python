#Exercício 103: Crie um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
    
def ficha(nome='', gols=0):
    if not nome:
        nome = '<Desconhecido>'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'

nome = str(input('Nome do jogador: ')).strip().capitalize()

gols = input('Numero de gols: ')
if gols.isnumeric():  # Verifica se a entrada é numérica
    gols = int(gols)
else:
    gols = 0
print(ficha(nome, gols))