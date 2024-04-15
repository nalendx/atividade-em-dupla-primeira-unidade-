class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    def calcular_area(self):
        return self.altura * self.largura
    
    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)

retangulo_exemplo = Retangulo(5, 10)
area = retangulo_exemplo.calcular_area()
perímetro = retangulo_exemplo.calcular_perimetro()
print("Área do retângulo:", area)
print("Perímetro do retângulo", perímetro)