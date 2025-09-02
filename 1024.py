def primeira_passada(string: str) -> str:
    saida = ''
    for char in string:
        if char.isalpha():
            value = ord(char)+3
            char = chr(value)
        else:
            pass
        saida+=char
    return saida
    
def segunda_passada(string: str) -> str:
    saida = ''
    pilha = []
    for char in string:
        pilha.append(char)
    for char in range(0, len(pilha)):
        saida += pilha.pop()
    return saida

def terceira_passada(string: str) -> str:
    saida = ''
    string = list(string)
    for i in range(0, len(string)):
        if i < len(string)//2:
            saida+=string[i]
            continue
        valor = ord(string[i]) - 1
        char = chr(valor)
        saida+=char
    return saida

def main(num: int):
    entrada = []
    for i in range(0, num):
        entrada.append(input())
    for i in range(0, len(entrada)):
        string = primeira_passada(entrada[i])
        string = segunda_passada(string)
        string = terceira_passada(string)
        print(string)

if __name__ == "__main__":
    num = int(input())
    main(num)
