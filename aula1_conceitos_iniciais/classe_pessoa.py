class Pessoa:
    def __init__(self):
        self.altura = 1.72
        self.idade = 25

    def correr(self):
        print('pessoa correndo')

    def comer(self):
        print('pessoa comendo')


pessoa1 = Pessoa()

pessoa1.comer()
