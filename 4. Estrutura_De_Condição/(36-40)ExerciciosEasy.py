

#Desafio 38 - Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: - O primeiro valor é maior - O segundo valor é maior - Não existe valor maior,os dois são iguais.
'''
num1 = int(input('Digite o primeiro Numero: '))
num2 = int(input('Digite o segundo Numero: '))

if (num1 > num2):
  print('Numero {} é Maior que {}'.format(num1, num2))
elif(num2 > num1):
  print('Numero {} é Maior que {}'.format(num2, num1))
elif (num1 == num2):
  print('\n\033[0;31mOs Dois Numeros Tem Valores Iguais')
'''
#Desafio 39 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''from datetime import date

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
'''
#Desafio 40 - crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9: RECUPERAÇÂO - Média 7.0 ou superior: APROVADO.
'''
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
'''