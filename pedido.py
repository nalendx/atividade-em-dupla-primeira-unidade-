class Pedido:
    def __init__(self, itens, total, status):
        self.itens = {}
        self.total = 0.0
        self.status = "Pendente"
    def adicionar_item(self, item, preco):
        if item in self.itens:
            self.itens[item] += preco
        else:
            self.itens[item] = preco
        self.total += preco
    def calcular_total(self):
        return self.total
    def alterar_status(self, novo_status):
        self.status = novo_status

pedido = Pedido()
pedido.adicionar_item("Hambúrguer", 10.0)
pedido.adicionar_item("Batata frita", 5.0)
pedido.adicionar_item("Refrigerante", 3.0)
print("Itens do pedido:", pedido.itens)
print("Total a ser pago:", pedido.calcular_total())
print("Status do pedido:", pedido.status)

pedido.alterar_status("Entregue")
print("Novo status do pedido:", pedido.status)   