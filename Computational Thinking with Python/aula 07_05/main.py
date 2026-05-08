# def media(a, b):

#     media1 = (a + b) / 2

#     return media1

# print(media(10, 15))
# print(media(5, 5))
# print(media(100, 130))


# print(media(float(input())))

def calculo(x, y):
    soma = x + y
    sub = x - y
    div = x / y
    mult = x * y
    media = (x + y) / 2

    return soma, sub, div, mult, media

a, b, c, d, e = calculo(100, 10)

print(a)
print(b)
print(c)
print(d)
print(e)