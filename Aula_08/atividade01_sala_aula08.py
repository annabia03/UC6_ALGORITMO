"""
Crie uma lista vazia;
Peça ao usuário digitar 3 itens;
Adicione cada item na lista;
Mostre todos os itens na lista final.
"""

# Laço de repetição;
# Método para manipular lista;
# Lista.

# Crie uma lista vazia chamada: compra
lista_compra = []

# Peça ao usuário digitar 3 itens
for i in range(3):
    item = input("Digite um item: ")
    # Adicione cada item na lista
    lista_compra.append(item)

print("Sua lista de compras: ")
# Mostre todos os itens da lista no final

for valor in lista_compra:
    print("-", valor)