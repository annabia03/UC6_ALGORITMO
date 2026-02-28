# Array (javascript) = Listas (python)

"""
dicionarios {} -> Para acessar dados usamos o nome da chave
listas [] -> Para acessar dados usamos a posição da lista
"""

notas = [10, 8, 5, 10, True, 7, "André"]
#         0  1  2   3    4   5     6

"""
 APPEND
"""
notas.append("SENAC")
print(notas)

"""
 INSERT
"""
notas.insert(0, False)
print(notas)

"""
 EXTEND
"""
nova_lista = ["Olá Mundo", 1980, 24.7]
nova_lista.extend(notas)
print(nova_lista)

"""
 REMOVE
"""
notas.remove(10)
print(notas)
notas.remove(True)
print(notas)
notas.remove("SENAC")
print(notas)
# notas.remove("andre")
# print(notas)
# o método remove e case sensitive


nomes_numeros = [390, "Adenilson", 19, "Anna", 45, "Iara", 390]
"""
 POP
"""
# nomes_numeros.pop(2) # o número 2 é a posição do nome Anna, que foi removido. Caso não coloque nenhuma posição, o pop sempre removerá a última informação!
# print(nomes_numeros)
"""
 CLEAR
 """
# print(nomes_numeros.clear())
# nomes_numeros.clear()
# print(nomes_numeros)

"""
 INDEX
 """
# print(nomes_numeros.index(390))
nomes_numeros.index(390)
print(nomes_numeros)

"""
 COUNT
 """
# print(nomes_numeros.count(390))
# nomes_numeros.count(390)
# print(nomes_numeros)


numeros = [34, 45, 67, 89, 43, 44, 26, 58, 66, 33, 90]

"""
 SORT
 """
numeros.sort()
print(numeros)
"""
 REVERSE
 """
numeros.reverse()
print(numeros)

"""
 SORT
 """
nomes = ["Adenilson", "Anna", "Beatriz", "Anne", "Bianca"]
nomes.sort()
print(nomes)

"""
 REVERSE
 """
nomes.reverse()
print(nomes)
