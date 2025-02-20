#Exercício 98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo, e realize a contagem.
#Seu programa tem que realizar três contagens através da função criada:
#   De 1 até 10, de 1 em 1.
#   De 10 até 0, de 2 em 2.
#   Uma contagem personalizada.

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if inicio > fim and passo > 0:
        passo = -passo
        
    for i in range(inicio, fim + (1 if passo > 0 else -1), passo):
        print(i ,end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    print('-=-'*10)

#Codigo principal
print('-=-'*10)
print('Contagem de 1 até 10 de 1 em 1')
contador(inicio=1, fim=10, passo=1)

print('Contagem de 10 até 0 de 2 em 2')
contador(inicio=10, fim=0, passo=2)

print('Agora é sua vez')
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
if p == 0:
    p = 1
print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
contador(i, f, p)