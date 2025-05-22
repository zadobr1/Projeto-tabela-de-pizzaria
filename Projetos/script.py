import pandas as pd
def listas(): #lista é o tanto de cadastro de pizza pré determinado
    lista = []
    total = sum(lista)
    cont = int(input("Quantas pizza serão cadastrada: "))
    for i in range(cont):
        casd = dict()
        casd['pizza'] = input('Qual e o Sabor da Pizza: ')
        casd['Borda'] = input(f'A {casd['pizza']} vai com borda? de : ')
        casd['Preço'] = float(input(f'Preço da Pizza da {casd['pizza']}: '))
        lista.append(casd)
    tot = pd.DataFrame(lista)
    total = tot['Preço'].sum()
    lista.append(total)
    return tot , total