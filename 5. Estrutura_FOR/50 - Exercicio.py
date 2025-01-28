# Desafio 50 - Desenvolva um programa que leia seis números e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.
s = 0
for i in range(0,6):
  num = int(input('Digite Um Numeros Inteiros: '))
  if num % 2 == 0:
    s += num
print('A soma dos Pares é: {}'.format(s))