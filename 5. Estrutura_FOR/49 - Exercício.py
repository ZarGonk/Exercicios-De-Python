# Desafio 49 - Refaça o desafio 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Qual Tabuada Voce Deseja: '))
for i in range(0, 11):
  tabuada = i * num
  print('{} x {} = {}'.format(i, num, tabuada))
