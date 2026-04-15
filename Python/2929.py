pilha = []
loop = int(input())
saida = []
for i in range (loop):
    entrada = list(map(str, input().split()))
    if entrada[0] == 'PUSH':
        pilha.append(int(entrada[1]))
    elif entrada[0] == 'MIN':
        if len(pilha) == 0:
            saida.append('EMPTY')
        else:
            saida.append(min(pilha))
    elif entrada[0] == 'POP':
        if len(pilha) == 0:
            saida.append('EMPTY')
        else:
            pilha.pop()
for i in saida:
    print(i)


