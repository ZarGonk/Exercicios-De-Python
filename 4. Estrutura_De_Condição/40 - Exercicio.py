# Desafio 40 - crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÂO - Média 7.0 ou superior: APROVADO.

nt = float(input('Primeira Nota: '))
nt2 = float(input('Segunda Nota: '))

media = (nt + nt2) / 2
print('Sua nota foi: {}'.format(media))

if media <= 5.0:
  print('Estude Mais Voce reprovou!!!')
elif 5.0 <= media <= 6.9:
  print('Vai para a recuperaçao :(')
elif media >= 7.0:
  print('Va de ferias querido!!!')
