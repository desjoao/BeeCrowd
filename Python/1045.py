def ordena(valores: list) -> list:
    for i in range(0, len(valores)-1):
        temp = valores[i]
        for j in range(i, len(valores)):
            if valores[j] > temp:
                temp = valores[j]
                valores[j] = valores[i]
                valores[i] = temp
    return valores

def tipo_triangulo(valores: str) -> list:
    valores = valores.split()
    saida = []
    for i in range(0, len(valores)):
        valores[i] = float(valores[i])
    valores = ordena(valores)
    if valores[0] >= valores[1]+valores[2]:
        saida.append('NAO FORMA TRIANGULO')
        return saida
    if valores[0]**2 == valores[1]**2 + valores[2]**2:
        saida.append('TRIANGULO RETANGULO')
    if valores[0]**2 > valores[1]**2 + valores[2]**2:
        saida.append('TRIANGULO OBTUSANGULO')
    if valores[0]**2 < valores[1]**2 + valores[2]**2:
        saida.append('TRIANGULO ACUTANGULO')
    if valores[0] == valores [1] == valores[2]:
        saida.append('TRIANGULO EQUILATERO')
    if valores[0] == valores[1] or valores[0] == valores[2] or valores[1] == valores[2]:
        saida.append('TRIANGULO ISOSCELES')
    return saida

if __name__ == "__main__":
    entrada = input()
    saida = tipo_triangulo(entrada)
    for i in range(0, len(saida)):
        print(saida[i])

