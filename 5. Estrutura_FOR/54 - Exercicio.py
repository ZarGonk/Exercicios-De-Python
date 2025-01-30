# Desafio 54 - Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Considerando 21 anos.
from datetime import date

maior = menor = 0

for i in range(0, 7):
  ano = int(input('Qual seu ano de nascimento: '))
  data = date.today().year
  idade = data - ano
  if idade >= 21:
    maior =+ 1
  else:
    menor =+ 1
print('São maior de idade: {}  \nSão menor de idade: {}'.format(maior, menor))
