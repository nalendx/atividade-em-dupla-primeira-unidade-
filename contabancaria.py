class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Deposito de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Valor de depósito inválido")
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
        else:
            print("Saldo insuficiente ou saque inválido.")
    def mostrar_saldo(self):
        print(f"Saldo atual da conta: {self.saldo}")

minha_conta = ContaBancaria("124356", "Pedro", 1000)
minha_conta = ContaBancaria("14356", "Maria", 1200 )
minha_conta.mostrar_saldo()
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.mostrar_saldo()




    
        