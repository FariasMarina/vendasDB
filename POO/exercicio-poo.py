
class Lata:
    def __init__(self, altura, diametro, volume, material='Alumínio', rotulo='Coca'):
        #material = "Alumínio" - ou seja - se não lançar nada, o que for colocado ali será o padrão
        #tem que ser os últimos atributos - são os DEFAULT.
        self.altura = altura
        self.diametro = diametro
        self.material = material
        self.rotulo = rotulo
        self.volume = volume
        self.lacre = True
        self.amassada = False
        self.aberta = False
        self.descartada = False

    def abrir(self):
        if self.aberta:
            print('Já está aberta')
        else:
            print('Clec, tsss...')
            self.aberta = True

    def retirar_lacre(self):
        if self.lacre and not self.descartada:
            print('Lacre retirado')
            self.lacre = False
        else:
            print('Já está sem lacre!')

    def beber(self, quantidade):
        if not self.aberta:
            print("A lata está fechada!")
        elif quantidade > self.volume:
            print(f'Você bebeu {self.volume} e ainda faltou {quantidade-self.volume}')
        else:
            self.volume -= quantidade
            print(f'Você bebeu {quantidade} e ainda restam {self.volume}')


    def esvaziar(self):
        if not self.aberta:
            print("Não dá pra esvaziar uma lata fechada")
        else:
            print(f'Lata vazia')
            self.volume = 0

    def amassar(self):
        if not self.amassada and self.volume == 0:
            print('Lata amassada')
            self.amassada = True
        else:
            print("Não dá pra amassar")

    def descartar(self):
        if self.descartada:
            print("Não dá pra descartar de novo")
        elif self.amassada:
            print("Descartada no lixeiro amarelo")
            self.descartada = True

        else:
            print('Primeiro amasse a lata')

l1 = Lata(12.5, 6, 350)


l1.abrir()
l1.beber(440)
l1.esvaziar()
l1.amassar()
l1.retirar_lacre()
l1.descartar()