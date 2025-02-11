
# aumentar(preço, taxa)
# diminuir(preço, taxa)
# dobro(preço)
# metade(preço)
def aumenta(preço, taxa):
    res = preço + ((taxa / 100) * preço)
    return res

def diminuir(preço, taxa):  
    res = preço - ((taxa / 100) * preço)
    return res

def dobro(preço):
    res =  preço * 2
    return res

def metade(preço):
    res = preço / 2
    return res
