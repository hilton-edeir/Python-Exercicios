
nome = input("Escreva: ")
lista_letras = []
palavra_revertida = ""

for letra in nome:
    lista_letras.append(letra)

lista_letras.reverse()

for letra in lista_letras:
    palavra_revertida += letra

print("Nome revertido: " + palavra_revertida)