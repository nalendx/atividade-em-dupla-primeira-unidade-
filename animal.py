class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie
     
    def falar(self, mensagem):
        return (f"{self.nome} está falando: {mensagem}")



if __name__ == "_main_":
    animal1 = Animal("lua", "4", "gato")
    animal2 = Animal("perola", "4","cachorro")
    print(animal1.falar("olá, sou um gato"))
    print(animal2.falar("e eu sou um cachorro"))