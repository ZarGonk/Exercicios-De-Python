# Desafio 41 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JÚNIOR - Até 25 anos: SÊNIOR - Acima: MASTER.
from datetime import date
data = int(input('Qual seu ano de Nascimento: '))
ano = date.today().year
idade = ano - data

if idade <= 9:
  print('Voce tem {} anos então pertence a categoria Mirim'.format(idade))
elif idade <= 14:
  print('Voce tem {} anos então pertence a categoria Infantil'.format(idade))
elif idade <= 19:
  print('Voce tem {} anos então pertence a categoria Junior'.format(idade))
elif idade <= 25:
  print('Voce tem {} anos então pertence a categoria Senior'.format(idade))
else:
  print('Voce tem {} anos então pertence a categoria Master'.format(idade))
