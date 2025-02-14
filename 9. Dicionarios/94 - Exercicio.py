# Exercício 94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#   Quantas pessoas foram cadastradas.
#   A média de idade do grupo.
#   Uma lista com todas as mulheres.
#   Uma lista com todas as pessoas com idade acima da média.

pessoas = list()
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
print('-=-'*15)