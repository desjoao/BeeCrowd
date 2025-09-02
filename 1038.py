menu = [0, 4.00, 4.50, 5.00, 2.00, 1.50]

def conta(pedido:str , qnt: str) -> float:
    pedido, qnt = int(pedido), float(qnt)
    valor = menu[pedido]*qnt/1.00
    return valor

if __name__ == "__main__":
    pedido = input()
    pedido = pedido.split(" ")
    print(f"Total: R$ {conta(pedido[0], pedido[1]):.2f}")
