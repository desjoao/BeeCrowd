def conta_inteiro(n: int) -> int:
    if n % 2 == 0:
        return 1
    return 0

def main() -> int:
    qnt = 0
    for i in range(5):
        num = int(input())
        qnt += conta_inteiro(num)
    return qnt

if __name__ == "__main__":
    print(f'{main()} valores pares')
