# Desafio 63 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
stop = cont = soma = 0

while stop != 999:
  num = int(input("Digite um numero (Para com 999): "))
  if num != 999:
    cont += 1  
    soma += num
  stop = num
print('Foram inseridos {} numero,e a soma entre eles é {}'.format(cont, soma))
