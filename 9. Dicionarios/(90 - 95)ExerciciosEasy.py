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







