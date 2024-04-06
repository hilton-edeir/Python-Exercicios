
nome = input("Insira o seu nome: ")
lista_letras = []
nome_reverso = ""

for letra in nome:
    lista_letras.append(letra)

lista_letras.reverse()

for letra in lista_letras:
    nome_reverso += letra

print("Nome revertido: " + nome_reverso)