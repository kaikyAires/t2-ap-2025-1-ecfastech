# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.
# A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5
# 5! = 5 . 4 . 3 . 2 . 1 = 120

numero = int(input("Fatorial de: "))

fatorial = 1
sequencia = ""

for i in range(numero, 0, -1):
    fatorial *= i
    if i == 1:
        sequencia += "1"
    else:
        sequencia += f"{i} . "

print(f"{numero}! = {sequencia} = {fatorial}")