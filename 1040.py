def media_basica(n1: float, n2: float, n3: float, n4: float) -> float:
    return (n1*2 + n2*3 + n3*4 + n4)/10

def media_final(n1: float, n2: float) -> float:
    return (n1+n2)/2

if __name__ == "__main__":
    notas = input()
    notas = notas.split(" ")
    for i in range(0, len(notas)):
        notas[i] = round(float(notas[i]), 1)
    media_1 = round(media_basica(notas[0], notas[1], notas[2], notas[3]), 1)
    if media_1 < 5:
        print(f"Media: {media_1}\nAluno reprovado.")
    elif media_1 >= 7:
        print(f"Media: {media_1}\nAluno aprovado.")
    else:
        prova_final = input()
        prova_final = round(float(prova_final), 1)
        media_2 = round(media_final(media_1, prova_final), 1)
        if media_2 >= 5:
            print(f"Media: {media_1}\nAluno em exame.\nNota do exame: {prova_final}\nAluno aprovado.\nMedia final: {media_2}")
        else:
            print(f"Media: {media_1}\nAluno em exame.\nNota do exame: {prova_final}\nAluno reprovado.\nMedia final: {media_2}")


