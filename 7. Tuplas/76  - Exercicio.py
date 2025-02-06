# Exercício 76: Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência. No final, mostre uma listagem de
#preços, organizando os dados em forma tabular.

compra = ('Bola',8, 'Chapeu', 5, 'Notebook', 2500, 'Roupas', 300)

print('Produto       |Preço     ')
for i in range(0, len(compra)):
    if i % 2 == 0:
        print(f'{compra[i]:.<15}',end=(''))
    else:
        print(f'R$ {compra[i]:.2f}')
