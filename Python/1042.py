def sort(valores: str) -> list:
    valores = valores.split(" ")
    for i in range(0, len(valores)):
        valores[i] = int(valores[i])
    for i in range(0, len(valores)-1):
        for j in range(i, len(valores)):
            if valores[i] > valores[j]:
                aux = valores[i]
                valores[i] = valores[j]
                valores[j] = aux
    return valores

if __name__ == "__main__":
    entrada = input()
    saida = sort(entrada)
    for valor in saida:
        print(valor)
    print('')
    for valor in entrada.split(" "):
        print(int(valor))

