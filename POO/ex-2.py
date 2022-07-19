# crie uma classe que modele um quadrado

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarValor(self,novoLado):
        self.lado = novoLado
        print(f'O valor antigo foi trocado para {novoLado}.')

    def retornarValor(self):
        print(f'O valor do lado é {self.lado}')

    def calcularArea(self):
        print(f'O valor da área é {self.lado * self.lado}')

q1 = Quadrado(int(input("Digite o valor do lado: ")))
q1.mudarValor(7)