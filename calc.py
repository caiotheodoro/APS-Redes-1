import sys
import funct as fc

def main():
    with open((sys.argv[1]), "r") as f:
        arquivo = [line.strip().split(" ") for line in f]
    if arquivo == None:
        print("Erro ao abrir o arquivo!!\n")
    else:
        print("Arquivo aberto com sucesso!!\n")

        # pega o endereço IP do arquivo e salva em ipAddr
        ipAddr = fc.replace(arquivo, 1)

        # pega o endereço da Máscara e salva em netMask
        netMask = fc.replace(arquivo, 2)

        # passa os dois valores para decimal
        fc.decimal(ipAddr)
        fc.decimal(netMask)

if __name__ == "__main__":
    main()
