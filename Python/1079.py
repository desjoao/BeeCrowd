class MediaPonderada:
    def __init__(self):
        self.__medias = []

    def calcula_medias(self, n: int):
        for i in range (0, n):
            entry = input().split()
            numbers = [float(x) for x in entry]
            self.__medias.append((numbers[0]*2 + numbers[1]*3 + numbers[2]*5) / 10)

    def imprime_medias(self, n: int):
        for i in range(0, n):
            print(f'{self.__medias[i]:.1f}')

if __name__ == '__main__':
    media_ponderada = MediaPonderada()
    n = int(input())
    media_ponderada.calcula_medias(n)
    media_ponderada.imprime_medias(n)
