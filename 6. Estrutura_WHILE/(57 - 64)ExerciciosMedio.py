#Desafio 57 - faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''op = str(input('Qual seu sexo[M/F]? ')).strip().upper()[0]

while op != 'M' and op != 'F':
  print('\nOpção Invalida so [M] ou [F]')
  op = str(input('Qual seu sexo[M/F]? ')).strip().upper()[0]
print('\nSexo {} Registrado com sucesso!!'.format(op))
'''







#Desafio 64 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''i = soma = maior = menor = 0
stop = ''

while stop != 'N':
  num = int(input('\nDigite um Numero: '))
  i += 1
  soma += num
  media = soma / i
  if i == 1:
    maior = num
    menor = num
  else:
    if num > maior:
      maior = num
    elif num < menor:
      menor = num
  stop = str(input('Deseja Continuar [S/N]? ')).strip().upper()[0]
print('\nA media entre os numeros digitados é: {}\nO maior é: {}\nO menor é: {}'.format(media, maior, menor))'''