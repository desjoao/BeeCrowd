def aumento(entrada: float) -> str:
    entrada = round(entrada, 2)
    reajuste = 0
    percentual = 0
    if entrada <=400:
        saida = round(entrada*1.15, 2)
        percentual = 15
    elif entrada <= 800:
        saida = round(entrada*1.12, 2)
        percentual = 12
    elif entrada <= 1200:
        saida = round(entrada*1.1, 2)
        percentual = 10
    elif entrada <= 2000:
        saida = round(entrada*1.07, 2)
        percentual = 7
    else:
        saida = round(entrada*1.04, 2)
        percentual = 4
    reajuste = round(saida - entrada, 2)
    return saida, reajuste, percentual

if __name__ == "__main__":
    entrada = float(input())
    saida, reajuste, percentual = aumento(entrada)
    print(f'Novo salario: {saida:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')
