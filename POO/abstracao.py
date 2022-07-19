from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, especie, habitat):
        self.especie = especie
        self.nome = nome
        self.habitat = habitat

    @abstractmethod #quando quer que seja obrigatoriamente lançada na classe filha
    def pedir_comida(self): #cada um faz de um jeito diferente
        return True

    def comer(self):
        print(f'{self.nome} comeu.')

    @staticmethod #é uma função que não precisa ter relação com o objeto, mas está dentro do código da classe
    #é mais questão de organização
    def nascer():
        print('Nasceu')

    @classmethod #chamar o método pra classe e não instância ex: Animal.morrer
    #tem que criar uma def pra isso apenas.
    def morrer(cls):
        print('Morreu')



class Felinos(Animal):
    def __init__(self, nome, especie, habitat, garras, orelhas):
        super().__init__(nome, especie, habitat)
        self.orelhas = orelhas
        self.garras = garras

    def pedir_comida(self): #cada um faz de um jeito diferente
        print('Miaaaauu')

gato = Felinos('Haru', 'gato', 'casa', True, 2)
gato.pedir_comida()
