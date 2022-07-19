from abc import ABC, abstractmethod

class Animais:
    def __init__(self, patas, tamanho, fome, nome, cor):
        self.patas = patas
        self.tamanho = tamanho
        self.fome = fome
        self.nome = nome
        self.cor = cor

    @abstractmethod
    def nascer(self):
        print('Nasceu!')

    def comer(self):
        if self.fome > 90:
            print('O animal não quer comer, está cheio')
        else:
            print("Minham, minham")

    def andar(self):
        print('O animal está caminhando')

class Felinos(Animais):
    def __init__(self, patas, tamanho, fome, nome, cor, domestico, felicidade):
        super().__init__(patas, tamanho, fome, nome, cor)
        self.domestico = domestico
        self.felicidade = felicidade

    def nascer(self):
        print('Nasceu!')

    def Cacar(self):
        if self.domestico:
            print('O animal foi caçar para brincar')
            self.felicidade += 50
        elif not self.domestico:
            print('O animal foi caçar e conseguiu uma presa.')
            self.felicidade += 70

    def dormir(self):
        print('O animal está nanando.')
        self.felicidade += 30


class Caninos(Animais):
    def __init__(self, patas, tamanho, fome, nome, cor, especie, adulto=True):
        super().__init__(patas, tamanho, fome, nome, cor)
        self.adulto = adulto
        self.especie = especie

    def nascer(self):
        print('Nasceu!')

    def comer(self):
        if self.fome < 100:
            print('Papou tudinho.')

    def reproduzir(self):
        if self.adulto:
            print('Você reproduziu um bebezinho!')
        else:
            print('Você ainda é um neném.')

class Reptil(Animais):
    def __init__(self, patas, tamanho, fome, nome, cor, habitat, acordado):
        super().__init__(patas, tamanho, fome, nome, cor)
        self.habitat = habitat
        self.acordado = acordado


    def nascer(self):
        print('Nasceu!')

    def atacar(self):
        if self.acordado:
            print('Atacou')
        else:
            print('Tá nanando, não tem como.')

    def dormir(self):
        print('Nanou o bichinho.')

    def acordar(self):
        print('Acordou o bichinho.')

class Ovinos(Animais):
    def __init__(self, patas, tamanho, fome, nome, cor, selvagem=False, pelado=False):
        super().__init__(patas, tamanho, fome, nome, cor)
        self.selvagem = selvagem
        self.pelado = pelado

    def nascer(self):
        print('Nasceu!')

    def pastar(self):
        if self.fome < 100:
            print('Minham minham, bom demais pastar.')
            self.fome = 100
        else:
            print('Não está muito afim.')

    def berrar(self):
        print('Béheheh!')


class SerHumano(Animais):
    def __init__(self, patas, tamanho, fome, nome, cor, cnh, idade):
        super().__init__(patas, tamanho, fome, nome, cor)
        self.cnh = cnh
        self.idade = idade

    def nascer(self):
        print('Nasceu!')

    def votar(self):
        if self.idade >= 16:
            print('Você votou com sucesso')
        else:
            print('Você não pode votar ainda!')

    def dirigir(self):
        if self.cnh:
            print('Vrummmm, você dirigiu e chegou ao local com sucesso')
        else:
            print('Vruummmm, você dirigiu e foi parado pela polícia logo em seguida. Game Over.')

#animais ao menos 4 atributos e 4 funções
#filhos - +2 atributos e +2 func
#felinos, caninos, réptil, ovinos, serhumano


#if não conseguiu caçar


tartaruga = Reptil(4, 'pequeno', 80, 'Zezinho', 'verde', 'lago', False)
tartaruga.atacar()
tartaruga.andar()
tartaruga.comer()
tartaruga.dormir()
print()
marcos = SerHumano(4,'grande', 92, 'Marcos', 'negro', False, 19)
marcos.comer()
marcos.andar()
marcos.dirigir()
print()
ovelha = Ovinos(4, 'médio', 36, 'Joelzinho', 'cinza', False, True)
ovelha.berrar()
ovelha.pastar()