# Desafio 61 - Melhore o DESAFIO 60 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

num = int(input('\nDigite o primeiro termo: '))
r = int(input('Qual a Razão da PA: '))
c = 0
mais = 10
total = 0
while mais != 0:
  total = total + mais
  while c <= total:  #Enquanto c for difente de 10 repita
    c = c + 1  #Contador
    an = num + (c - 1) * r  #Faz a PA
    print(an, end=' -> ')

  print('PAUSA!!!')
  mais = int(input('\nQuantos termos a mais voce quer:'))

print('ACABOU!!!')