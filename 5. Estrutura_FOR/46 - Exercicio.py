# Desafio 46 - Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for i in range(10, -1, -1):
  print('{} ...'.format(i))
  sleep(0.5)
print('\nOLHA EXLOSÂO\nQUANDO ELA BATE COM A BUNDA NO CHÃO')
