def tempo_jogo(hora_ini: int, minuto_ini: int, hora_fim: int, minuto_fim: int) -> str:
    if minuto_fim < minuto_ini:
        hora_fim -=1
        minuto_fim += 60
    if hora_fim < hora_ini:
        hora_fim +=24
    horas = hora_fim - hora_ini
    minutos = minuto_fim - minuto_ini
    if horas == 0 and minutos == 0:
        horas = 24
    msg = f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)"
    return msg

if __name__ == "__main__":
    entrada = input()
    entrada = entrada.split(" ")
    for i in range(0, len(entrada)):
        entrada[i] = int(entrada[i])
    print(tempo_jogo(entrada[0], entrada[1], entrada[2], entrada[3]))

