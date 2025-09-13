def ordena_palavras(string: str) -> str:
    string = string.split(" ")
    for i in range(0, len(string) -1):
        for j in range(i, len(string)):
            if len(string[i]) < len(string[j]):
                aux = string[i]
                string[i] = string[j]
                string[j] = aux
    saida = ""
    for palavra in string:
        saida+= palavra + " "
    return saida

if __name__ == "__main__":
    string = input()
    string = ordena_palavras(string)
    print(string)
