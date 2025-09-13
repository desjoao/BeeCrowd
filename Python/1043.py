def verifica_triangulo(valores: list) -> float:
    valores = valores.split()
    for i in range(0, len(valores)):
        valores[i] = float(valores[i])
    maior = valores[0]
    soma = 0
    for i in range (0, len(valores)):
        if valores[i] > maior:
            maior = valores[i]
        soma += valores[i]
    if soma > 2*maior:
        perimetro = round(soma, 1)
        return f"Perimetro = {perimetro}"
    else:
        area = round((valores[0] + valores[1])*valores[2]/2, 1)
        return f"Area = {area}"

if __name__ == "__main__":
    entrada = input()
    print(verifica_triangulo(entrada))
