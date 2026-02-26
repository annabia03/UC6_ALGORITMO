# Dicionário em Python

aluno = {
    # "chave" : valor
    "nome": "Pedro",
    "idade": 19,
    "nota": 8,
    "curso": "TÉCNICO EM INFORMÁTICA PARA INTERNET",
    # Array
    "array": [30, True, "Texto"],
    #          0    1       2
    # Dicionario dentro de outro dicionario
    "endereco": {
        "cidade": "SP",
        "estado": "SP",
        "numero": 234
    }
}

# mostra dicionario principal
print(aluno)

# retorna nome do aluno
print(aluno["nome"])

# retorna o array
print(aluno["array"])

# retorna o endereço, estamos acessando um dicionario dentro de outro dicionario
print(aluno["endereco"])

# acessar apenas um unico dado do endereco
print(aluno["endereco"]["estado"])

#acessando campo especifico dentro de um array
print(aluno["array"][1])

# ALTERAR DADOS DO DICIONARIO
aluno["idade"] = 20
print(aluno["idade"])

# Alterar dados dentro de um array que esta dentro do dicionario
aluno["array"[2]] = 9
print(aluno["array"][2])
print(aluno["array"])

# Alterar dados do dicionarioo endereço que esta dentro do dicionario aluno
# Sempre que precisar acessar uma chave dentro de um dicionario usaremos colchetes
aluno["endereco"]["cidade"] = "São Paulo"
print(aluno["endereco"])
print(aluno["endereco"]["cidade"])

# ADICIONAR UM NOVO CAMPO
aluno["periodo"] = "Noturno"
print(aluno)

# Deletar uma informação
del aluno["idade"]
print(aluno)

# Percorrer um dicionario usando laço de repetição
for chave in aluno:
    print(chave)

# Percorrer um dicionario usando laço de repetição para retornar os valores
for valor in aluno.values():
    print(valor)

# Percorrer um dicionario e retornar chave e valor
for chave, valor in aluno.items():
    print(chave, ":", valor)
