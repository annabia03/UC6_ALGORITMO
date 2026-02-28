"""
Crie uma lista com 4 nomes;
Peça ao usuário um nome para remover;
Se o nome existir, remova;
Mostre a lista final.
"""

lista_nomes = ["Anna", "Leandro", "Hannah", "Lúcia"]

print("Lista de nomes:", lista_nomes)

nome_remover = input("Digite um dos nomes da lista para remover: ")

if nome_remover in lista_nomes:
    lista_nomes.remove(nome_remover)

print(lista_nomes)

