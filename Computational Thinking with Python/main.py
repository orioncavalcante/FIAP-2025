dados = [[], [], [], [], []]
contador = 0

while contador < 4:
    print(f"\nDados do {contador + 1}º carro:")

    marca = input("Digite a marca do carro: ")
    dados[0].append(marca)

    versao = input("Digite a versão do carro: ")
    dados[1].append(versao)

    ano = int(input("Digite o ano do carro: "))
    dados[2].append(ano)

    cor = input("Digite a cor do carro: ")
    dados[3].append(cor)

    ipva = input("O IPVA foi pago? (s/n0: )").lower()
    dados[4].append(ipva)

    contador += 1

print(dados)
    
