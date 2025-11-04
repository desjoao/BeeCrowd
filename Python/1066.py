def paridade(n: int, par: int, impar: int) -> int:
    if n%2==0:
        par +=1
    else:
        impar +=1
    return par, impar

def sinal(n:int, pos: int, neg: int) -> int:
    if n > 0:
        pos +=1
    elif n < 0:
        neg +=1
    return pos, neg

def main() -> int:
    par, impar, pos, neg = 0, 0, 0, 0
    for i in range(5):
        n = int(input())
        par, impar = paridade(n, par, impar)
        pos, neg = sinal(n, pos, neg)
    return par, impar, pos, neg

if __name__ == "__main__":
    par, impar, pos, neg = main()
    print(f'{par} valor(es) par(es)\n{impar} valor(es) impar(es)')
    print(f'{pos} valor(es) positivo(s)\n{neg} valor(es) negativo(s)')
