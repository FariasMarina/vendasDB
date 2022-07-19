# especificar quanto vai usar de gasolina em determinada kilometragem.

class Carro():
    def __init__(self, kmlt, combustivel=0):
        self.kmlt = kmlt
        self.__combustivel = combustivel

    def andar(self, km):
        consumoEmLitros = km / self.kmlt

        if self.__combustivel >= consumoEmLitros:
            print(f'Seu carro andou {km} kms.')
            self.__combustivel -= consumoEmLitros
        else:
            print('O carro não tem gasolina.')

    def adicionarGasolina(self, lt):
        self.__combustivel += lt
        print('Gasolina adicionada com sucesso.')

    def conferirGasolina(self):
        print(self.__combustivel)


c1 = Carro(20)
c1.andar(7)
c1.adicionarGasolina(4)
c1.andar(79)
c1.conferirGasolina()

# meuFusca = Carro(15);  # 15 quilômetros por litro de combustível.
# meuFusca.adicionarGasolina(20);  # abastece com 20 litros de combustível.
# meuFusca.andar(100);  # anda 100 quilômetros.
# meuFusca.obterGasolina()  # Imprime o combustível que resta no tanque.
