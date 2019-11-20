# DIRETÓRIO: FUNCT.PY
# ALUNOS: ALISSON E CAIO
# NESTE ARQUIVO TEMOS TODAS AS FUNCOES UTILIZADAS PARA O DESENVOLVIMENTO DA APS
# INCIALMENT: FUNCOES DE TRATAMENTO DE DADOS:

# funcao que auxilia na inicialização


def replace(arquivo, posicao):
    variavel = arquivo[posicao][1]  # peega o valor
    variavel = variavel.replace('"', '')  # substitui as aspas por nada
    variavel = variavel.replace(',', '')  # substitui a vitgula por nada

    return variavel

# funcao que faz a passagem dos enderecos para decimal


def decimal(endereco):
    # corto o endereco em 4 partes, com o delimitador sendo o '.'
    endereco_decimal = [int(endereco.split(".")[0]), int(endereco.split(
        ".")[1]), int(endereco.split(".")[2]), int(endereco.split(".")[3])]

    return endereco_decimal

# funcao que faz a passagem dos enderecos para binario


def binario(endereco):
    endereco_binario = [int(endereco.split(".")[0]), int(endereco.split(
        ".")[1]), int(endereco.split(".")[2]), int(endereco.split(".")[3])]
    # passo os valores para binário e verifico caso algum seja igual a vazio, se for dou o valor 0 para ele
    p0 = d2b(int(endereco_binario[0]))
    if p0 == "":
        p0 = 0

    p1 = d2b(int(endereco_binario[1]))
    if p1 == "":
        p1 = 0

    p2 = d2b(int(endereco_binario[2]))
    if p2 == "":
        p2 = 0

    p3 = d2b(int(endereco_binario[3]))
    if p3 == "":
        p3 = 0

    #print(p0, p1, p2, p3)
    # concateno todos em uma única variável
    endereco_binario = [str(p0), str(p1), str(p2), str(p3)]

    return endereco_binario

# funcao recursiva que passa um valor decimal para binario


def d2b(n):
    if n == 0:
        return ''
    else:
        return d2b(n//2) + str(n % 2)

# FUNCOES PARA AS IMPLEMENTACOES EM QUESTAO:

# motor do codigo


def execucao(ipAddr, netMask):
    # variaveis para salvar no arquivo final
    arquivo = open("saida.txt", "w")

    # lista do ipAddr decimal
    ipAddr_Dlist = []
    ipAddr_Dlist = decimal(ipAddr)
    # print(ipAddr_Dlist)

    # lista do netMask decimal
    netMask_Dlist = []
    netMask_Dlist = decimal(netMask)
    # print(netMask_Dlist)

    # lista do ipAddr binario
    ipAddr_Blist = []
    ipAddr_Blist = binario(ipAddr)
    # print(ipAddr_Blist)

    # lista do netMask binario
    netMask_Blist = []
    netMask_Blist = binario(netMask)
    # print(netMask_Blist)

    arquivo.write("Classe do IP: ")
    # pega a classe do ip
    classeIp = classe_ip(ipAddr_Dlist)
    print(classeIp)
    arquivo.write(classeIp + "\n")

    if ((mask_validation(netMask_Blist) == True) & (ip_validation(ipAddr_Blist) == True)):
        print("Ainda não concluído...")

# funcao que verifica se a mascara da rede e valida


def mask_validation(endereco):
    for i in range(0, (len(endereco) - 1)):
        for j in range(i + 1, (len(endereco) - 1)):
            if(endereco[j] > endereco[i]):
                return False
    return True

# funcao que verifica se o ip da rede e valido


def ip_validation(endereco):
    return True

# funcao que verifica a classe do IP


def classe_ip(endereco):
    A = False
    errA = False
    a = "A"
    errAA = "O endereço aparenta ser da classe A, porém é inválido!"
    B = False
    errB = False
    b = "B"
    errBB = "O endereço aparenta ser da classe B, porém é inválido!"
    C = False
    errC = False
    c = "C"
    errCC = "O endereço aparenta ser da classe C, porém é inválido!"
    err = "Endereco invalido"

    if ((endereco[0] <= 126) and (endereco[0] > 0)):
        A = True
        if(((endereco[1] == 0) and (endereco[2] == 0) and (endereco[3] == 0)) or ((endereco[1] == 255) and (endereco[2] == 255) and (endereco[3] == 355))):
            errA = True

    if ((endereco[0] <= 191) and (endereco[0] > 127)):
        B = True
        if(((endereco[2] == 255) and (endereco[3] == 255)) or ((endereco[2] == 0) and (endereco[3] == 0))):
            errB = True

    if ((endereco[0] <= 223) and (endereco[0] > 191)):
        C = True
        if((endereco[3] < 1) and (endereco[3] > 254)):
            errC = True

    if ((A == True) and (errA == False)):
        return a
    elif ((A == True) and (errA == True)):
        return errAA
    elif ((B == True) and (errB == False)):
        return b
    elif ((B == True) and (errB == True)):
        return errBB
    elif ((C == True) and (errC == False)):
        return c
    elif ((C == True) and (errC == True)):
        return errCC
    else:
        return err



#calcula o Ip da rede


def calc_ipRede(ipAddr_Dlist,netMask_Dlist):
    ipRede[]
    for i in range(4):
    ipRede[i] =  ipAddr_Dlist[i] & netMask_Dlist[i]
    return ipRede


#calcula o broadcast