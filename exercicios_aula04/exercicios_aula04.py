# Crie um algoritmo que leia dois números inteiros e  verifique qual é maior e qual é o menor e imprima o resultado no terminal.

numero1 = int(input("Digite o primeiro numero inteiro: "))
numero2 = int(input("Digite o segundo numero inteiro: "))

if numero1 > numero2:
    print(f"O numero {numero1} é maior que o numero {numero2}!")

else:
    print(f"O numero {numero1} é menor que o numero {numero2}!")


# Estações do ano
# Crie um algoritmo onde o usuário digita um número de 1 até 12 e retorne em tela qual é o mês correspondente a ele:
# Exemplo de entrada: 4
# Exemplo de saída: Abril

numero = int(input("Digite um numero de 1 ate 12: "))

if numero == 1:
    print(f"O numero {numero} corresponde ao mes de Janeiro!")

elif numero == 2:
    print(f"O numero {numero} corresponde ao mes de Fevereiro!")

elif numero == 3:
    print(f"O numero {numero} corresponde ao mes de Março!")

elif numero == 4:
    print(f"O numero {numero} corresponde ao mes de Abril!")

elif numero == 5:
    print(f"O numero {numero} corresponde ao mes de Maio!")

elif numero == 6:
    print(f"O numero {numero} corresponde ao mes de Junho!")

elif numero == 7:
    print(f"O numero {numero} corresponde ao mes de Julho!")

elif numero == 8:
    print(f"O numero {numero} corresponde ao mes de Agosto!")

elif numero == 9:
    print(f"O numero {numero} corresponde ao mes de Setembro!")

elif numero == 10:
    print(f"O numero {numero} corresponde ao mes de Outubro!")

elif numero == 11:
    print(f"O numero {numero} corresponde ao mes de Novembro!")

elif numero == 12:
    print(f"O numero {numero} corresponde ao mes de Dezembro!")



# Crie um programa em Python que receba um número inteiro do usuário e determine: “É par ou é ímpar?”
# O programa deve exibir na tela se o número informado é par ou ímpar.

numero = int(input("Digite um numero inteiro: "))

if numero % 2 == 0:
    print(f"O numero {numero} é par!")

else:
    print(f"O numero {numero} é impar!")