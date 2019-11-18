def replace(arquivo, posicao):
    variavel = arquivo[posicao][1] # peega o valor
    variavel = variavel.replace('"', '') # substitui as aspas por nada
    variavel = variavel.replace(',', '') # substitui a vitgula por nada

    return variavel

def decimal(endereco):
    # corto o endereco em 4 partes, com o delimitador sendo o '.'
    p1 = int(endereco.split(".")[0])
    p2 = int(endereco.split(".")[1])
    p3 = int(endereco.split(".")[2])
    p4 = int(endereco.split(".")[3])
    print("Decimal:\n", p1, p2, p3, p4)

    # passo os valores para binário e verifico caso algum seja igual a vazio, se for dou o valor 0 para ele
    p1 = d2b(p1)
    if p1 == "":
        p1 = 0
    
    p2 = d2b(p2)
    if p2 == "":
        p2 = 0

    p3 = d2b(p3)
    if p3 == "":
        p3 = 0
    
    p4 = d2b(p4)
    if p4 == "":
        p4 = 0

    # concateno todos em uma única variável
    endereco_binario = str(p1) + "." + str(p2) + "." + str(p3) + "." + str(p4)
    print("Binário:\n", endereco_binario, "\n")

def d2b(n):
    if n == 0:
        return ''
    else:
        return d2b(n//2) + str(n%2)