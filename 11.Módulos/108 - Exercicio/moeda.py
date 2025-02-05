
# aumentar(preço, taxa)
# diminuir(preço, taxa)
# dobro(preço)
# metade(preço)
def aumenta(preço=0, taxa=0):
    res = preço + ((taxa / 100) * preço)
    return res

def diminuir(preço=0, taxa=0):  
    res = preço - ((taxa / 100) * preço)
    return res

def dobro(preço=0):
    res =  preço * 2
    return res

def metade(preço =0):
    res = preço / 2
    return res

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')