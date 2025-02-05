
# aumentar(preço, taxa)
# diminuir(preço, taxa)
# dobro(preço)
# metade(preço)
def aumenta(preço=0, taxa=0, form=False):
    res = preço + ((taxa / 100) * preço)
    return res if form is False else moeda(res)

def diminuir(preço=0, taxa=0, form=False):  
    res = preço - ((taxa / 100) * preço)
    return res if form is False else moeda(res)
    
def dobro(preço=0, form=False):
    res =  preço * 2
    return res if form is False else moeda(res)

def metade(preço =0, form=False):
    res = preço / 2
    return res if form is False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')