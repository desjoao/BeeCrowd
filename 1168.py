leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def num_leds(entrada:str) -> str:
    cont = 0
    entrada = list(entrada)
    for i in range (0, len(entrada)):
        cont+=leds[int(entrada[i])]
    return cont

if __name__ == "__main__":
    num = int(input())
    valores = []
    for i in range(0, num):
        valores.append(input())
    for i in range(0, len(valores)):
        saida = num_leds(valores[i])
        print(f"{saida} leds")
