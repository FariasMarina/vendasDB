
class bomba_Combustivel:
    def __init__(self, valor_Litro, quantidade_Combustivel, tipo_Combustivel='gasolina'):
        self.tipo_Combustivel = tipo_Combustivel
        self.valor_Litro = valor_Litro
        self.quantidade_Combustivel = quantidade_Combustivel

    def abastecer_Por_Valor(self, valor):
        print(f'O valor de R${valor} retornará {valor / self.valor_Litro} litros.')
        qtdval = valor / self.valor_Litro
        self.alterar_Qtde_Combustivel(qtdval)

    def abastecer_por_Litro(self, litros):
        print(f'O valor a ser pago é de {litros * self.valor_Litro}')
        qtdltr = litros * self.valor_Litro
        self.alterar_Qtde_Combustivel(qtdltr)

    def alterar_Valor(self, novoValor):
        print(f'O valor antigo {self.valor_Litro} foi substituído por {novoValor}')
        self.valor_Litro = novoValor

    def alterar_Combustivel(self, novoTipo):
        print(f'O combustível {self.tipo_Combustivel} foi alterado para {novoTipo}')


    def alterar_Qtde_Combustivel(self,alt_litros):
        self.quantidade_Combustivel -= alt_litros
        print(f'Quantidade atual de combustível: {self.quantidade_Combustivel}litros')

b1 = bomba_Combustivel(5.76, 50)
b1.abastecer_Por_Valor(30)