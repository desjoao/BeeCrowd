n = int(input())
dentro = 0
fora = 0
for i in range(n):
    val = int(input())
    if val >= 10  and val <= 20:
        dentro +=1
    else:
        fora +=1

print(f'{dentro} in\n{fora} out')
