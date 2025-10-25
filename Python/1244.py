def ordena_frase(entrada: str) -> list:
    lista = list(map(str, entrada.split()))
    for i in range(0, len(lista)-1):
        maior = len(lista[i])
        for j in range(len(lista)-1, i-1, -1):
            if len(lista[j]) >= maior:
                maior = len(lista[j])
                ref = j
        valor = lista.pop(ref)
        lista.insert(i, valor)
    return lista

if __name__ == '__main__':
    vezes = int(input())
    lista_saida = []
    for i in range(vezes):
        lista = ordena_frase(input())
        saida = ''
        for palavra in lista:
            saida+=palavra+' '
        lista_saida.append(saida[:-1])
    for frase in lista_saida:
        print(frase)

            
