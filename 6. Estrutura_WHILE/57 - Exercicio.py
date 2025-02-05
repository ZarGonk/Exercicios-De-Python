# Desafio 57 - faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
op = str(input('Qual seu sexo[M/F]? ')).strip().upper()[0]

while op != 'M' and op != 'F':
  print('\nOpção Invalida so [M] ou [F]')
  op = str(input('Qual seu sexo[M/F]? ')).strip().upper()[0]
print('\nSexo {} Registrado com sucesso!!'.format(op))








