# Ex 2
# numero = True
# 
# if numero == True:
#     print("Faça alguma coisa!")
# else:
#     print("Faça outra coisa")


# Ex 3

# temperatura = float(input("Digide a temperatura: "))
# frio = False

# frio = temperatura < 18

# print("Está frio" if frio else "Não está frio")


# Ex 4

# senha = input("Digite sua senha: ")

# senha_correta = "1234"

# if senha == senha_correta:
#     print("Senha correta")
# else:
#     print("Senha Incorreta")    


# Ex 5

# numero = int(input("Digite um número: "))

# par = numero %2 == 0

# if par:
#     print("O número digitado é par")
# else:
#     print("O número digitado é ímpar")


# Ex 6

salario = float(input("Digite seu salário: "))

salario1 = salario <= 2000
salario2 = salario > 2000 and salario <= 3500
salario3 = salario > 3500 and salario <= 5000
salario4 = salario > 5000

desconto = 0

if salario1:
    print(f"Seu salário é de R${salario}. Não terá desconto.\nSalário final = R${salario}")
elif salario2:
    desconto = salario * 0.10
    print(f"Seu salário é de R${salario}. Desconto de 10% aplicado!\nSalário final = R${salario - desconto}")
elif salario3:
    desconto = salario * 0.20
    print(f"Seu salário é de R${salario}. Desconto de 20% aplicado!\nSalário final = R${salario - desconto}")
elif salario4:
    desconto = salario * 0.275
    print(f"Seu salário é de R${salario}. Desconto de 27,5% aplicado!\nSalário final = R${salario - desconto}")
else:
    print("Erro")