def tipo_de_animal(tipo_1: str, tipo_2: str, tipo_3: str) -> str:
    if tipo_1.lower() == 'vertebrado':
        if tipo_2.lower() == 'ave':
            if tipo_3.lower() == 'carnivoro':
                print('aguia')
            else:
                print('pomba')
        else:
            if tipo_3.lower() == 'onivoro':
                print('homem')
            else:
                print('vaca')
    else:
        if tipo_2.lower() == 'inseto':
            if tipo_3.lower() == 'hematofago':
                print('pulga')
            else:
                print('lagarta')
        else:
            if tipo_3.lower() == 'hematofago':
                print('sanguessuga')
            else:
                print('minhoca')

if __name__ == "__main__":
    entrada_1 = input()
    entrada_2 = input()
    entrada_3 = input()
    tipo_de_animal(entrada_1, entrada_2, entrada_3)

