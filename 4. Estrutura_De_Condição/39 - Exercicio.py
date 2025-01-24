# Desafio 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

print('-----------------ALISTAMENTO-----------------')
print('==='*15)

ano = int(input("\nDigite Seu Ano De Nascimento: "))
data = date.today().year #Data Atual
idade = data - ano

#Compara a idade se é menor que 18
if idade < 18:
  falta = 18 - idade
  print('\nDaqui a algum tempo vai chegar a sua vez!!!\n\n\033[0;31mFalta {} Anos'.format(falta))
#Compara a idade se é igual a 18
elif idade == 18:
  print('\033[0;32mVoce deve ir se alistar, \033[1;31mAGORA CORREE!!!')
#Compara a idade se é maior que 18
elif idade > 18:
  print('\nJa se Alistou?\n\n1 - Sim\n2 - Não')
  num = int(input('sim ou nao? '))
  if num == 1:
    print('\nTa salvo')
  elif num == 2:
    passou = idade - 18
    print('\nTA DORMINDO FDP,ja passou o tempo\nTa a {} Anos Atrasado'.format(passou))
