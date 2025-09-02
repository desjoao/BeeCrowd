def idade(dias: int) -> int:
    ano = dias//365
    mes = (dias%365)//30
    dia = (dias%365)%30
    return ano, mes, dia
    
if __name__ == "__main__":
    entrada = int(input())
    anos, meses, dias = idade(entrada)
    print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")
