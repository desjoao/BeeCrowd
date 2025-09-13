def verifica_multiplicidade(valores: list) -> str:
    valores = valores.split()
    for i in range(0, len(valores)):
        valores[i] = int(valores[i])
    valores = sort(valores)
    if valores[1]%valores[0] == 0:
        return 'Sao Multiplos'
    return 'Nao sao Multiplos'

def sort(valores: list) -> list:
    for i in range(0, len(valores)-1):
        temp = valores[i]
        for j in range(i, len(valores)):
            if valores[j] < temp:
                temp = valores[j]
                valores[j] = valores[i]
                valores[i] = temp
    return valores

if __name__ == "__main__":
    entrada = input()
    print(verifica_multiplicidade(entrada))
