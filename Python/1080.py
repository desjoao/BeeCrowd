class MaiorValor:
    def __init__(self):
        self.__index = -1
        self.__maior_valor = -1

    def setter(self, index: int, valor: int):
        self.__index = index
        self.__maior_valor = valor

    def getter(self) -> int:
        return self.__index, self.__maior_valor

    def printer(self):
        index, maior_valor = self.getter()
        print(f'{maior_valor}\n{index}')
    
    def reader(self):
        for i in range(1, 101):
            index, maior_valor = self.getter()
            n = int(input())
            if n > maior_valor:
                self.setter(i, n)

if __name__ == '__main__':
    mv = MaiorValor()
    mv.reader()
    mv.printer()
