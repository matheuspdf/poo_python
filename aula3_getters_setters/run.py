class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        self.__elem = None

    def setter(self, valor: int) -> None:
        self.__valor = valor

    def getter(self) -> int:
        return self.__valor


my_class = MinhaClasse()

my_class.setter(43)
valor = my_class.getter()
print(valor)