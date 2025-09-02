def intervalo(numero: float) -> str:
    if numero >=0 and numero <=100.0000:
        if numero <=25.0000:
            return "[0, 25]"
        elif numero <=50.0000:
            return "(25, 50]"
        elif numero <=75.0000:
            return "(50, 75]"
        else:
            return "Intervalo (75, 100]"

    else:
        return "Fora de intervalo"

if __name__ == "__main__":
    entrada = float(input())
    print(intervalo(entrada))
