class Tamagotchi:
    def __init__(self, nome, fome, idade , saude):
        self.nome = nome
        self.fome = fome
        self.idade = idade
        self.saude = saude
# - ALTERAR
    def alterarNome(self, novoNome):
        print(f'O nome {self.nome} foi alterado para {novoNome}')
        self.nome = novoNome

    def alterarFome(self,novaFome):
        print(f'A nova fome é {novaFome}')

    def alterarSaude(self,novaSaude):
        print(f'A nova saúde é {novaSaude}')

    def alterarIdade(self,novaIdade):
        print(f'A nova idade é {novaIdade}')

# - RETORNAR

    def retornarNome(self):
        print(f'O nome do seu Tamagotchi é {self.nome}.')

    def retornarFome(self):
        print(f'A fome do seu Tamagotchi é {self.fome}')

    def retornarSaude(self):
        print(f'A saúde do seu Tamagotchi é {self.saude}.')

    def retornarIdade(self):
        print(f'A idade do seu Tamagotchi é {self.idade} anos.')

    def humor(self):
        if self.saude >= 70 and self.fome <= 30:
            print(f'{self.nome} está feliz!')
        elif self.saude >= 50 and self.fome <= 50:
            print(f'{self.nome} está meio cabisbaixo.')
        elif self.saude >= 20 and self.fome <= 80:
            print(f'{self.nome} está mal!')
        elif self.saude >= 1 and self.fome <= 6:
            print(f'Atenção, {self.nome} está em alto risco!')
        else:
            print(f'Poxa... {self.nome} não está entre nós.')

t1 = Tamagotchi('Josiel', 2, 3, 70)
t1.humor()
t1.retornarSaude()
t1.retornarFome()