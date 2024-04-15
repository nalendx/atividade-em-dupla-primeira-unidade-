class Estudante:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        else:
            return sum(self.notas) / len(self.notas)
    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return f"{self.nome} foi aprovado em média {media:.2f}"
        else:
            return f"{self.nome} foi reprovado em média {media:.2f}"
notas_aluno = [7.5, 8.0, 6.5, 9.0]
aluno = Estudante("João", 20, notas_aluno)
print("Média das notas:", aluno.calcular_media())
print(aluno.verificar_aprovacao())
        