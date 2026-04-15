soma_pos = 0
qnt = 0
for i in range(6):
    n = float(input())
    if n >0:
        soma_pos+= n
        qnt+=1
media = round(soma_pos/qnt, 1)
print(f'{qnt} valores positivos\n{media}')
