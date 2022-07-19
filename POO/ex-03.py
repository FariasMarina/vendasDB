#crie uma class que modele um retângulo

# DENTRO DA CLASSE NÃO PODE INPUT

class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, novo_ladoA, novo_ladoB):
        self.ladoA = novo_ladoA
        self.ladoB = novo_ladoB
        print(f'Seus novos valores são {self.ladoA, self.ladoB}')

    def valorDosLados(self):
        print(f' Lado A: {self.ladoA} e lado B {self.ladoB}')

    def calcularArea(self):
        print(f'A área do retângulo é {self.ladoA * self.ladoB}')

    def calcularPerimetro(self):
        print(f' O perímetro do quadrado é {self.ladoA + self.ladoB}')

medida_b = int(input("Digite a medida do lado maior do piso: "))
medida_h = int(input("Digite a medida do lado menor do piso: "))

r1 = Retangulo(medida_h, medida_b)


print(f'A quantidade de piso necessário é {medida_h * medida_b}')
print(f'A quantidade de rodapé necessário é {(medida_h + medida_b) * 2} metros.')
