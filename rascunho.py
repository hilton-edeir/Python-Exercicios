
'''
#Imprimir dados a partir do índice de uma lista
lista_cores = ["Red", "Green", "White", "Black"]

print("\nPrimeira cor: %s " %lista_cores[0])
print("Última cor: %s"  %lista_cores[-1])
'''

primeira_data = input("\nInsira a primeira data no formato DD/MM/AAAA: ")
segunda_data = input("Insira a segunda data no formato DD/MM/YYYY: ")

lista_primeira_data = primeira_data.split("/")
lista_segunda_data = segunda_data.split("/")

dia_diferenca = abs(int(lista_primeira_data[0]) - int(lista_segunda_data[0]))
mes_diferenca = abs(int(lista_primeira_data[1]) - int(lista_segunda_data[1]))
ano_diferenca = abs(int(lista_primeira_data[2]) - int(lista_segunda_data[2]))

if dia_diferenca == 0 and mes_diferenca == 0 and ano_diferenca == 0:
    print("\nExiste 0 dia entre ", primeira_data, " e ", segunda_data)

if dia_diferenca > 0 and mes_diferenca == 0 and ano_diferenca == 0:
    print("\nExiste ", dia_diferenca, "dia(s) entre ", primeira_data, " e ", segunda_data)

if dia_diferenca == 0 and mes_diferenca > 0 and ano_diferenca == 0:
    print("\nExiste", mes_diferenca, "month(s) entre ", primeira_data, " e ", segunda_data)

elif dia_diferenca == 0 and mes_diferenca == 0 and ano_diferenca > 0:
    print("\nExiste ", ano_diferenca, "ano(s) entre ", primeira_data, " e ", segunda_data)

elif dia_diferenca > 0 and mes_diferenca > 0 and ano_diferenca > 0:
    print("\nExiste %i dia(s) %i mes(es) e %i ano(s) entre %s e %s" % (dia_diferenca, mes_diferenca, ano_diferenca, primeira_data, segunda_data))
