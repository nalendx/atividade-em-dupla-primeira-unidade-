#dupla Natália Fiorentino e Natália Alencar
class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def ligar(self):
        return f"{self.modelo} ligou"
    def desligar(self):
        return f"{self.modelo} desligou"
    def acelerar(self):
        return f"{self.modelo} acelerou"

if __name__ == "__main__":
    carro1 = Carro("Fiat", "Fusca", "1994", "Vermelho")
    carro2= Carro("Chevorlet", "Celta", "2006", "Cinza")

    print(carro1.ligar())
    print(carro1.desligar())
    print(carro2.acelerar())