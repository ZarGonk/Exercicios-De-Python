# Desafio 55 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = menor = 0

for i in range(0, 5):
  num = float(input('{} - Qual O seu peso (KG): '.format(i+1)))
  if i == 0:
    maior = num
    menor = num
  else:
    if maior <= num:
      maior = num
    elif menor >= num:
      menor = num
print('O maior peso é: {:.1f}Kg\nO menor peso é: {:.1f}Kg'.format(maior, menor))
