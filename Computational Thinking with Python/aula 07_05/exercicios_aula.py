# 1.

# def converter_c_to_f(c):
#     cf = (9*c)/5 + 32
#     return cf

# print(converter_c_to_f(20))


# 2.

# a1, a2, a3, a4 = map(float, input("Digite as 4 notas separadas por espaço: ").split())

# def calcula_media(n1, n2, n3, n4):
#     return (n1 + n2 + n3 + n4) / 4

# print(f"Média: {calcula_media(a1, a2, a3, a4)}")


# 3.
v1, v2, v3, v4, v5 = map(float, input("insira 5 valores separados por espaço: ").split())

def calcula_media(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

print(f"Média: {calcula_media(v1, v2, v3, v4, v5)}")
