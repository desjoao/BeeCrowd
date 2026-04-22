class Tabuada():
    def __init__(self):
        self._tabuada = []

    def define_tabuada(self, n: int):
        for i in range (1, 11):
            self._tabuada.append(n*i)

    def imprime_tabuada(self, n: int):
        for i in range (1, 11):
            print(f'{i} x {n} = {self._tabuada[i-1]}')

if __name__ == '__main__':
    n = int(input())
    tabuada = Tabuada()
    tabuada.define_tabuada(n)
    tabuada.imprime_tabuada(n)
