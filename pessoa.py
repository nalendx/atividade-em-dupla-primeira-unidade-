class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def definir_nome(self, nome):
        self.nome = nome

    def definir_idade(self, idade):
        self.idade = idade

    def definir_altura(self, altura):
        self.altura = altura

    def obter_nome(self):
        return self.nome

    def obter_idade(self):
        return self.idade

    def obter_altura(self):
        return self.altura

    def cumprimentar(self):
        return f"Olá! Meu nome é {self.nome}. Prazer em conhecê-lo!"


pessoa = Pessoa("Natália", 16, 1, 64)
print("Nome:", pessoa.obter_nome())
print("Idade:", pessoa.obter_idade())
print("Altura:", pessoa.obter_altura())
print(pessoa.cumprimentar())
