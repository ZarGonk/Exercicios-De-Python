# Desafio 58 - Crie um programa que leia dois valores e mostre um menu na tela: [1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
v1 = int(input('1° Valor: ')) 
v2 = int(input('2° Valor: '))
op = 0

while op != 5:
  op = int(input('\n-------Qual Opcão deseja:-------\n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa.\n\nOpção: '))

  if op == 1: #Soma 2 numeros
    s = v1 + v2
    print('\nA soma de {} + {} = {}'.format(v1, v2, s))
  elif op == 2: #Multiplica 2 numeros
    m = v1 * v2
    print('\nA multiplicação de {} x {} = {}'.format(v1, v2, m))
  elif op == 3: #Acha o maior entre 2 numeros 
    if v1 > v2:
      maior = v1
      print('\n{} > {}'.format(v1, v2))
    else:
      maior = v2
      print('\n{} > {}'.format(v2, v1))
  elif op == 4: #Pede novos numeros
    v1 = int(input('1° Valor: ')) 
    v2 = int(input('2° Valor: '))
  else:
    print('\nOpção Invalidade Tente Novamente')
  op = int(input('\n-------Qual Opcão deseja:-------\n[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa.\n\nOpção: '))
print('Fim do programa')  