n = int(input())
for i in range(6):
    if n % 2 == 0:
        print(n+2*i+1)
    else:
        if i == 0:
            print(n)
        else:
            print(n+2*i)
