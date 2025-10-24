dia_1 = int(list(input().split())[1])
tempo_1 = list(map(int, input().split(":")))
dia_2 = int(list(input().split())[1])
tempo_2 = list(map(int, input().split(":")))

diff_dia = dia_2-dia_1
diff_horas = tempo_2[0] - tempo_1[0]
diff_minutos = tempo_2[1] - tempo_1[1]
diff_segundos = tempo_2[2] - tempo_1[2]
if diff_segundos < 0:
    diff_segundos += 60
    diff_minutos-=1
if diff_minutos < 0:
    diff_minutos+=60
    diff_horas-=1
if diff_horas < 0:
    diff_horas += 24
    diff_dia -=1
print(f'{diff_dia} dia(s)\n{diff_horas} hora(s)\n{diff_minutos} minuto(s)\n{diff_segundos} segundo(s)')