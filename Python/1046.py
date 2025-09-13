## Leia a hora inicial e a hora final de um jogo. Calcular a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.

def calcula_tempo(entrada: str) -> str:
    entrada = list(entrada.split(' '))
    for i in range (0, len(entrada)):
        entrada[i] = int(entrada[i])
    if entrada[0] > entrada[1]:
        diff = 24 - entrada [0] + entrada[1]
    else:
        diff = abs(entrada[0] - entrada[1])
        if diff == 0: 
            diff = 24
    msg = f'O JOGO DUROU {diff} HORA(s)'
    return msg

if __name__ == "__main__":
    entrada = input()
    print(calcula_tempo(entrada))

