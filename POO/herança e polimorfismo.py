class Veiculo:
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo):
        self.cor = cor
        self.lugares = lugares
        self.qtd_pneus = qtd_pneus
        self.tipo_motor = tipo_motor
        self.valor = valor
        self.ano = ano
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print('Acelerou')

    def frear(self):
        print('Freou')

    def ligar(self):
        print('Ligou')

    def desligar(self):
        print('Desligou')

class Moto(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, empinada=False):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.empinada = empinada

    def empinar(self):
        if self.empinada:
            print('Já está empinada')
        else:
            print('IMPINAAAAA')
            self.empinada = True

    def desempinar(self):
        if self.empinada:
            print('Você desempinou')
            self.empinada = False
        else:
            print('Não está empinada.')

m1 = Moto('preta', 2, 2, '125CC', 17000, 2022, 'Honda', 'CG-125')

print(m1.tipo_motor)
m1.empinar()
v1 = Veiculo('Preto', 4, 3, '180CV', 45000, 2012, 'Chevrolet', 'Celta')


class Carro(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, dir_autonoma=True, eletrico=True):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.dir_autonoma = dir_autonoma
        self.eletrico = eletrico

    def drift(self):
        print('Você driftou!')

    def carregar(self):
        if self.eletrico:
            print('Você carregou seu veículo 100%.')
        else:
            print('Seu carro não é elétrico.')


class Onibus(Veiculo):
    def __init__(self, cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo, portas, andares):
        super().__init__(cor, lugares, qtd_pneus, tipo_motor, valor, ano, marca, modelo)
        self.portas = portas
        self.andares = andares

    def pararNaProeb(self):
        while True:
            print('Aguarde a liberação pra sair')

    def dirigir(self):
        print('Você está dirigindo o 12.')



o1 = Onibus('branco', 32, 4, 'sla', 80000, 2022, 'mercedes-benz', 'modelobus', 3, 1)

