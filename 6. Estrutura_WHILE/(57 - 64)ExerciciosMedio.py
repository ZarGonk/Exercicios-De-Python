#Desafio 57 - faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''op = str(input('Qual seu sexo[M/F]? ')).strip().upper()[0]

while op != 'M' and op != 'F':
  print('\nOpção Invalida so [M] ou [F]')
  op = str(input('Qual seu sexo[M/F]? ')).strip().upper()[0]
print('\nSexo {} Registrado com sucesso!!'.format(op))
'''



#Desafio 61 - Melhore o DESAFIO 60 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

'''num = int(input('\nDigite o primeiro termo: '))
r = int(input('Qual a Razão da PA: '))
c = 0
mais = 10
total = 0
while mais != 0:
  total = total + mais
  while c <= total:  #Enquanto c for difente de 10 repita
    c = c + 1  #Contador
    an = num + (c - 1) * r  #Faz a PA
    print(an, end=' -> ')

  print('PAUSA!!!')
  mais = int(input('\nQuantos termos a mais voce quer:'))

print('ACABOU!!!')
'''
#Desafio 62 - Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#num = int(input('Digite um numero inteiro: '))
'''print('    Sequencia de Fibonacci')
print('-='*15)
  
  num = int(input("Quantos Numeros Deseja Mostrar: "))
  t1 = 0
  t2 = 1
  
  c = 3
  print('{} -> {}'.format(t1, t2), end='')
  while c <= num:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
  print(' \nfim')'''

#Desafio 63 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''stop = cont = soma = 0

while stop != 999:
  num = int(input("Digite um numero (Para com 999): "))
  if num != 999:
    cont += 1  
    soma += num
  stop = num
print('Foram inseridos {} numero,e a soma entre eles é {}'.format(cont, soma))
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