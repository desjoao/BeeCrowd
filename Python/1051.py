def primeiro(valor: float) -> float:
    return 0

def segundo(valor:float) -> float:
    return round(valor*0.08, 2)

def terceiro(valor: float) -> float:
    return round(valor*0.18, 2)

def quarto(valor: float) -> float:
    return round(valor*0.28, 2)

def main(entrada: str) ->str:
    entrada = round(float(entrada), 2)
    saida = 0
    if entrada <= 2000:
        saida = primeiro(entrada)
        return saida
    entrada -= 2000
    if entrada < 1000:
        saida += segundo(entrada)
        return saida
    saida += segundo(1000)
    entrada -= 1000
    if entrada < 1500:
        saida+= terceiro(entrada)
        return saida
    saida+= terceiro(1500)
    entrada-=1500
    saida+= quarto(entrada)
    return saida

if __name__ == "__main__":
    valor = main(input())
    if valor == 0:
        print('Isento')
        exit()
    print(f'R$ {valor:.2f}')


