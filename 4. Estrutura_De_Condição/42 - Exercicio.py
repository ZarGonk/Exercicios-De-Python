# Desafio 42 - Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - Equilátero: todos os lados iguais - Isósceles: dois lados iguais - Escaleno: todos os lados diferente.

a = float(input('Digite primeiro numero: '))
b = float(input('Digite segundo numero: '))
c = float(input('Digite terceiro numero: '))

#verifica se pode formar um trinagulo
if a < b + c and b < a + c and c < a + b:
  print('\nPode formar um tringulo')
  #Verifica o tipo do triangulo
  if a == b == c:
    print('\nEsse triangulo é Equilatero')
  elif a == b or b == c or a == c:
    print('\nEsse trinagulo é Isosceles')
  else:
    print('\nEsse triangulo é Escaleno')
else:
  print('\nNao forma um triangulo')
