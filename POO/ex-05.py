class Macaco():
    def __init__(self, nome, bucho=[]):
        self.nome = nome
        self.bucho = bucho


    def comer(self, comida):
        print(f'O macaco comeu {comida}.')
        self.bucho.append(comida)

    def verBucho(self):
        if not self.bucho:
            print("Não tem comida no bucho.")
        else:
            print(f'O que tem de comida no bucho é {self.bucho}')

    def digerir(self):
        print(f'Digestão concluída com sucesso.')
        self.bucho = ''


m1 = Macaco('Marcelo')
m2 = Macaco('Rodrigo')

m1.comer('pão')
m1.comer('arroz')
m1.comer(m2.nome)
m1.verBucho()
m1.digerir()
m1.verBucho()


# colocar verbo em nome de função - colocar no infinitivo(aumentar, alterar, diminuir)