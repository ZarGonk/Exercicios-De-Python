
# aumentar(preço, taxa)
# diminuir(preço, taxa)
# dobro(preço)
# metade(preço)
def aumentar(preço=0, taxa=0, form=True):
    res = preço + ((taxa / 100) * preço)
    return res if form is False else moeda(res)

def diminuir(preço=0, taxa=0, form=True):  
    res = preço - ((taxa / 100) * preço)
    return res if form is False else moeda(res)
    
def dobro(preço=0, form=True):
    res =  preço * 2
    return res if form is False else moeda(res)

def metade(preço=0, form=True):
    res = preço / 2
    return res if form is False else moeda(res)

def moeda(preço=0, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')

def resumo(preço=0, aumenta=10, diminui=5):
    print('-'*30)
    print('RESUMO DE VALOR'.center(30))
    print('-'*30)
    print(f'Preço Analisado:   {moeda(preço)}')
    print(f'{aumenta}% de aumento:    {aumentar(preço,aumenta)}')
    print(f'{diminui}% de redução:    {diminuir(preço,diminui)}')
    print(f'Dobro do preço:    {dobro(preço)}')
    print(f'Metade do preço:   {metade(preço)}')
    print('-'*30)
    
