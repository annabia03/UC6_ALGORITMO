# Criar um dicionário com dados digitados pelo usuário.
#Peça ao usuário:
# nome;
# idade;
# cidade;
# Guarde em um dicionário e mostre na tela

nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))
cidade_usuario = input("Digite sua cidade: ")

usuario = {
    "nome": nome_usuario,
    "idade": idade_usuario,
    "cidade": cidade_usuario

}

print("Informações: ")
print(usuario)


# Criar um dicionário com dados digitados pelo usuário.
#• nome do aluno
#• nota1
#• nota2
#• nota3
#• nota4
#• nota5
#Depois calcule e mostre a média.

nome_aluno = input("Digite aqui o nome do aluno: ")
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
nota4 = int(input("Digite a quarta nota: "))
nota5 = int(input("Digite a quinta nota: "))

soma = nota1 + nota2 + nota3 + nota4 + nota5
"""
média dessas 5 notas
"""
media = (soma / 5)

aluno = {
    "nome": nome_aluno,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3,
    "nota4": nota4,
    "nota5": nota5,
    "media": media
}

print(aluno)