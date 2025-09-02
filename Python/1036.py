def bhaskara(entradas: list) -> float:
    try:
        delta = entradas[1]**2 - 4*entradas[0]*entradas[2]
        raiz_a = (-1*entradas[1]+ (delta)**(1/2))/(2*entradas[0])
        raiz_b = (-1*entradas[1]- (delta)**(1/2))/(2*entradas[0])
        return round(raiz_a, 5), round(raiz_b, 5)
    except Exception as e:
        print(str(e))
        return None, None

if __name__ == "__main__":
    entrada = input()
    entrada = entrada.split(" ")
    lista = []
    for i in range(0, len(entrada)):
        lista.append(round(float(entrada[i]), 5))
    raiz_a, raiz_b = bhaskara(lista)
    print(f"R1 = {raiz_a}\nR2 = {raiz_b}")
