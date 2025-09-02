def notas_moedas(valor: float) -> list:
    saida = [0]*12
    notas = valor//1
    moedas = round(valor - notas, 2)
    print(moedas)
    while notas >0:
        if notas - 100 >= 0:
            saida[0] += 1
            notas -= 100
            continue
        elif notas - 50 >= 0:
            saida[1] += 1
            notas -= 50
            continue
        elif notas - 20 >= 0:
            saida[2] += 1
            notas -= 20
            continue
        elif notas - 10 >= 0:
            saida[3] += 1
            notas -= 10
            continue
        elif notas - 5 >= 0:
            saida[4] += 1
            notas -=5
            continue
        elif notas - 2 >= 0:
            saida[5] +=1
            notas -= 2
            continue
        else:
            saida[6] +=1
            notas -= 1
            continue
    while moedas >0:
        moedas = round(moedas, 2)
        if moedas - 0.5 >= 0:
            saida[7]+=1
            moedas -= 0.5
            continue
        elif moedas - 0.25 >= 0:
            saida[8]+=1
            moedas -= 0.25
            continue
        elif moedas - 0.1 >= 0:
            saida[9]+=1
            moedas -= 0.1
            continue
        elif moedas - 0.05 >= 0:
            saida[10]+=1
            moedas -= 0.05
            continue
        else:
            saida[11]+=1
            moedas -= 0.01
            continue
    return saida
if __name__ == "__main__":
    entrada = float(input())
    qnt = notas_moedas(entrada)
    print(f"NOTAS:\n{qnt[0]} nota(s) de R$ 100.00\n{qnt[1]} nota(s) de R$ 50.00\n{qnt[2]} nota(s) de R$ 20.00\n{qnt[3]} nota(s) de R$ 10.00\n{qnt[4]} nota(s) de R$ 5.00\n{qnt[5]} nota(s) de R$ 2.00\nMOEDAS:\n{qnt[6]} moeda(s) de R$ 1.00\n{qnt[7]} moeda(s) de R$ 0.50\n{qnt[8]} moeda(s) de R$ 0.25\n{qnt[9]} moeda(s) de R$ 0.10\n{qnt[10]} moeda(s) de R$ 0.05\n{qnt[11]} moeda(s) de R$ 0.01")

