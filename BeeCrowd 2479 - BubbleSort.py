while True:
    try:
        notas, consultas = input().split(" ")
        notas = int(notas)
        consultas = int(consultas)
        vN = [0]*100
        vC = [0]*100


        for i in range (0, notas):
            vN[i] = int(input())
            if not vN[i]:
                break
            elif (vN[i] < 0):
                vN[i]*=(-1)

        for i in range (0, notas):
            for j in range(i, notas):
                if vN[i] < vN[j]:
                    temp = vN[j]
                    vN[j] = vN[i]
                    vN[i] = temp

        for i in range (0, consultas):
            vC[i] = int(input())
            if not vC[i]:
                break
            elif (vC[i] < 0):
                vC[i]*= (-1)


        for i in range(0, consultas):
            print(vN[vC[i]-1])
    except EOFError:
        break

