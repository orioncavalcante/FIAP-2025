class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando Objeto
p1 = Pessoa("Ana", 25)
p2 = Pessoa("Paulo", 32)

# Mostrar a informação

p1.mostrar()
p2.mostrar()