class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = float(preco)
        self.estoque = int(estoque)

    def atualizar_estoque(self, quantidade):
        self.estoque += quantidade

    def calcular(self, quantidade):
        return self.preco * quantidade

if __name__ == "_main_":
    produto1 = Produto("arroz", 5.0, 10)
    produto2 = Produto("feijão", 8.0, 10)

    produto1.calcular(5)
    print(f"Novo estoque de {produto2.nome}: {produto1.estoque}")

    preco_total = produto2.calcular(3)
    print(f"Preço total de {produto2.nome}: R${preco_total}")