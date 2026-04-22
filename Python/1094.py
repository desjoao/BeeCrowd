if __name__ == '__main__':
    n = int(input())
    coelhos = 0
    ratos = 0
    sapos = 0
    for i in range(0, n):
        resp = input().split(' ')
        if resp[1] == 'C':
            coelhos += int(resp[0])
        elif resp[1] == 'R':
            ratos += int(resp[0])
        else:
            sapos += int(resp[0])
    cobaias = coelhos + ratos + sapos 
    print(f'Total: {cobaias} cobaias')
    print(f'Total de coelhos: {coelhos}')
    print(f'Total de ratos: {ratos}')
    print(f'Total de sapos: {sapos}')
    print(f'Percentual de coelhos: {coelhos*100/cobaias:.2f} %')
    print(f'Percentual de ratos: {ratos*100/cobaias:.2f} %')
    print(f'Percentual de sapos: {sapos*100/cobaias:.2f} %')

