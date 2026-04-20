def resto_dois(n: int) -> list:
    lista = []
    if n == 1:
        lista.append(2)
        return lista
    if n == 2:
        return lista
    i = 0
    for j in range(0, n):
        if j%n == 2:
            i = j
            break
    while i <= 10000:
        lista.append(i)
        i+=n
    return lista

def imprime_dividendos(lista: list):
    if len(lista) == 0:
        return
    for i in lista:
        print(i)

if __name__ == '__main__':
    n = int(input())
    imprime_dividendos(resto_dois(n))
