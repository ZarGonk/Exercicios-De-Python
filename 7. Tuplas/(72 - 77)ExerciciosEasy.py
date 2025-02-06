#Exercício 72: Crie um programa que tenha uma tupla totalmente preenchida 
# com uma contagem por extenso, de zero até vinte. O programa deverá ler 
# um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um numero: '))

if 0 <= num <= 20:
    print(f'O numero {num} por extenso fica {numero[num]}')
else:
    print(f'Numero {num} nao encontrado')'''



#Exercício 74: Crie um programa que vai gerar cinco números aleatórios e 
# colocar em uma tupla. Depois disso, mostre a listagem dos números gerados
#e também indique o menor e o maior valor que estão na tupla.
'''from random import randint

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
print(f'O Maior é {max(aleatorio)}')'''

#Exercício 75: Desenvolva um programa que leia quatro valores pelo teclado 
#e guarde-os em uma tupla. No final, mostre:
#   Quantas vezes apareceu o valor 9.
#   Em que posição foi digitado o primeiro valor 3.
#   Quais foram os números pares.
'''num1 = int(input('Digite 1 valor: '))
num2 = int(input('Digite 1 valor: '))
num3 = int(input('Digite 1 valor: '))
num4 = int(input('Digite 1 valor: '))

tupla = (num1, num2, num3, num4)

#Quantas vezes o 9 apareceu e se apareceu
if 9 in tupla:
    nove = tupla.count(9)
    print(f'O 9 apareceu {nove} vezes')
else:
    print('Não teve ocorrência só 9')

#Qual posição o 3 apareceu e se apareceu    
if 3 in tupla:
    tres = tupla.index(3)+1
    print(f'primeira aparição do 3: {tres}°')
else:
    print('Numero 3 não foi encontrado')    

#Ve se tem par e mostra se tiver
print(f'Numero Par: ') 
for i in tupla:
    if i % 2 == 0:
        print(i ,end=' ')  '''

#Exercício 76: Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência. No final, mostre uma listagem de
#preços, organizando os dados em forma tabular.
'''compra = ('Bola',8, 'Chapeu', 5, 'Notebook', 2500, 'Roupas', 300)

print('Produto       |Preço     ')
for i in range(0, len(compra)):
    if i % 2 == 0:
        print(f'{compra[i]:.<15}',end=(''))
    else:
        print(f'R$ {compra[i]:.2f}')'''

#Exercício 77: Crie um programa que tenha uma tupla com várias palavras 
#(não usar acentos). Depois disso, você deve mostrar, para cada palavra, 
#quais são suas vogais.
palavras = ("banana", "livro", "oceano", "montanha", "tecnologia", 
            "criatividade", "viagem", "planeta", "futuro", "aventura")

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')