import calendar

data = input("\nInsira uma data no formato MM/AAAA: ")
lista_data = data.split("/")

print("")
print(calendar.month(int(lista_data[1]), int(lista_data[0])))