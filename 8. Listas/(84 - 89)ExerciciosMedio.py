#Exercício 84: Faça um programa que leia nome e peso de várias pessoas, 
#guardando tudo em uma lista. No final, mostre:
#   Quantas pessoas foram cadastradas.
#   Uma listagem com as pessoas mais pesadas.
#   Uma listagem com as pessoas mais leves.
'''dados   = list()
pessoas = list()
maior = menor = 0

while True:
    dados.append(str(input('Enter your name: ')))
    dados.append(float(input('Enter your weight: ')))

    pessoas.append(dados [:])
    dados.clear()

    stop = str(input('Want to stop[Y/N]: ')).strip().upper()
    if stop == 'Y':
         break

maior = menor = pessoas[0][1]

for p in pessoas:
    if p[1] > maior:
          maior = p[1]
    if p[1] < menor:
         menor = p[1]

print(f'Total number of registered people was: {len(pessoas)}')
print(f'The bigger weight registered was: {maior} of people: ',end='')
for p in pessoas:
     if maior == p[1]:
          print(p[0],end='...')
print(f'\nThe minor weight registered was: {menor} of people: ',end='')
for p in pessoas:
     if menor == p[1]:
          print(p[0],end='...')'''






