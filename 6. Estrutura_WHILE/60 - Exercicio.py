# Desafio 60 - Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('        Gerador de PA')
print('-='*15)
num = int(input('Digite o primeiro termo: '))
r = int(input('Qual a Razão da PA: '))

c = 0

while c != 10:
  c = c + 1
  an = num + (c - 1) * r
  print(an, end=' -> ')
print('ACABOU!!!')
