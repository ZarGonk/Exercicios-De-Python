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