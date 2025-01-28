# Desafio 48 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
for i in range(1, 501):
  if i % 2 != 0 and i % 3 == 0:
    s = s + i

print('A Soma dentre os impares,multiplos de 3 é: {}'.format(s))

#OUUU

"""S = 0
for i in range(1, 500, 2):
    if (i%3) == 0 :
        S += i
print(S)"""
