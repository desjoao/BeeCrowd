def seleciona(lista: str) -> str:
    args =lista.split(" ")
    for i in range(0, len(args)):
        args[i] = int(args[i])
    print(args)
    if args[1]> args[2] and args[3]> args[0] and args[2] + args[3] > args[1] + args[0] and args[2] > 0 and args[3] > 0 and args[0]%2==0:
        return 'Valores aceitos'
    else:
        return 'Valores nao aceitos'
if __name__ == "__main__":
    msg = seleciona(input())
    print(msg)
