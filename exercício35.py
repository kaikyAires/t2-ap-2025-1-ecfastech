# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
# existentes entre 1 e um número inteiro informado pelo usuário.
limite = int(input("Digite um número inteiro para gerar os números primos até ele: "))

print(f"\nNúmeros primos entre 1 e {limite}:")

for num in range(2, limite + 1):
    primo = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(num, end=" ")

print() 