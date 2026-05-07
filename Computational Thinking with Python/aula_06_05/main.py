# MATCH / CASE

comando = 'start'

if comando == 'start':
    print('Iniciar')
elif comando == 'stop':
    print('parar')
else:
    print('Erro')

####################################

match comando:
    case "start":
        print('iniciar')
    case "stop":
        print("Parar")
    case _:
        print("Erro")

###################################

opcao = input("Insira 1 ou 2: ")

match opcao:
    case "1":
        print("Cadastrar!")
    case "2":
        print("Listar!")
    case _:
        print("Valor inválido!")

###################################

dados = ['produto', 'arroz', 10]

match dados:
    case("produto", nome, qtd):
        print(f"{nome} - {qtd}")
    case _:
        print("formato inválido")

###################################

lista = [1, 2, 3]

match lista:
    case [1, 2, 3]:
        print("Lista completa!")
    case _:
        print("Lista incompleta")

###################################
tipo = "A"
status = "ativo"

if tipo == 'A' and status == 'ativo':
    print("faça alguma coisa!")
elif tipo == 'B' and status == 'inativo':
    print("faça outra coisa")

match (tipo, status):
    case ("A", "Ativo"):
        print("faça alguma coisa")
    case ("B", "inativo"):
        print("Faça outra coisa")

###################################
numero = int(input("Insira um número"))

match numero:
    case _ if numero  %2 == 0:
        print("par")
    case _:
        print("impar")