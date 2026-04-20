n = int(input())
array = []
while n > 0:
    array.append(int(input()))
    n-=1

for i in range(0, len(array)):
    x = array[i]
    if x >0:
        if x %2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    elif x == 0:
        print("NULL")
    else:
        if x %2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")

