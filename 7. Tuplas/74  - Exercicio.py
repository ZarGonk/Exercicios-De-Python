# Exercício 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem dos números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint

num  = randint(1, 100)
num1 = randint(1, 100)
num2 = randint(1, 100) 
num3 = randint(1, 100)
num4 = randint(1, 100)

aleatorio = (num, num1, num2, num3, num4)
ordenado = sorted(aleatorio)

print(f'Os números são:\n{aleatorio}')
print(f'O Menor é {ordenado[0]}')
print(f'O Maior é {ordenado[4]}')
#outro jeito
print(f'O menor é {min(aleatorio)}')
print(f'O Maior é {max(aleatorio)}')
