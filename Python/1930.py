def tomadas(entrada: str) ->int:
    entrada = list(entrada.split())
    saida = 0
    for i in range(0, len(entrada)):
        saida += int(entrada[i]) -1
    
    return saida + 1

if __name__ == "__main__":
    entrada = input()
    print(tomadas(entrada))
