class Bola:
    def __init__(self,cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, novaCor):
        print(f'A cor {self.cor} foi trocada para {novaCor}.')
        self.cor = novaCor

    def mostraCor(self):
        print(f'A cor é {self.cor}')


b1 = Bola('azul', 55, 'Plástico')
b1.trocaCor('Rosa')