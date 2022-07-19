#programação estruturada
#programação orientada a objetos
#classe para um veículo
#Sempre começa classe com letra maiúscula(por convenção)

#self: instância
class Veiculo:
    #cor, porta, marca, modelo, ano
    def __init__(self, cor, porta, marca, modelo, ano):
        self.cor = cor
        self.porta = porta
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
#para printar bonitinho sem aparecer o o local no espaço na memória
    def __repr__(self):
        return repr(f'{self.marca} - {self.modelo} - {self.porta} - {self.cor} - {self.ano}')

    def ligar(self):
        print(f'Vruuum, vruuum pro {self.modelo}')

    def desligar(self):
        print(f'Acabou vruum vruumm pro {self.modelo}')

#instanciar um objeto:

veiculos = []

for _ in range(2):
    cor = input('Digite a cor:' )
    porta = input('Digite a qtde de portas:' )
    marca = input('Digite a marca: ' )
    modelo = input('Digite o modelo: ' )
    ano = input('Digite o ano: ' )

    cadastro = Veiculo(cor, porta, marca, modelo, ano)
    veiculos.append(cadastro)

print(repr(veiculos))