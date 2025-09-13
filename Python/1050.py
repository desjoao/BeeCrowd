ddd = {
        "11": "Sao Paulo",
        "19": "Campinas",
        "21": "Rio de Janeiro",
        "27": "Vitoria",
        "31": "Belo Horizonte",
        "32": "Juiz de Fora",
        "61": "Brasilia",
        "71": "Salvador"
        }

def define_cidade(entrada: str) -> str:
    return ddd.get(entrada)

if __name__ == "__main__":
    entrada = input()
    cidade = define_cidade(entrada)
    if not cidade:
        print('DDD nao cadastrado')
        exit()
    print(cidade)
