def coordenadas(x: float, y: float) -> str:
    if x < 0:
        if y > 0:
            return 'Q2'
        elif y < 0:
            return 'Q3'
        else:
            return 'Eixo X'

    elif x > 0:
        if y > 0:
            return 'Q1'
        elif y < 0: 
            return 'Q4'
        else:
            return 'Eixo X'
    else:
        if y != 0:
            return 'Eixo Y'
        else:
            return 'Origem'
if __name__ == "__main__":
    entradas = input()
    entradas = entradas.split(" ")
    for i in range(0, len(entradas)):
        entradas[i] = round(float(entradas[i]), 1)
    print(coordenadas(entradas[0], entradas[1]))


