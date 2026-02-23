#  você terá que criar um algoritmo utilizando laço de repetição e estrutura condicional para criar uma tabuada, seguindo as seguintes regras:
# Seu programa precisa receber um número digitado pelo usuário, verifique se esse número é válido, se o número for válido então use 
# o laço de repetição para mostrar a tabuada utilizando o número que o usuário digitou se o número for inválido então mostrar a 
# mensagem “Número invalido, tente novamente”

numero_tabuada = input("Digite um número: ")

# retorna true se o que o usuario digitou for numerico
#ele nao valida numero negativo e nem numero decimal

if numero_tabuada.isdigit() > 0:
    numero_tabuada = int(numero_tabuada)
    print(f"Tabuada do numero {numero_tabuada}: ")

    for numero in range(1, 11):
        resultado = numero_tabuada * numero
        print(f"{numero_tabuada} x {numero} = {resultado}")

else:
    print("Número iválido, digite outro entre 1 e 10!")
