# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
# O programa deverá mostrar também o número de divisões que ele executou para encontrar os números
# primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Digite um número inteiro: "))

divisoes_total = 0
primos = []

for numero in range(2,n + 1):
    divisoes = 0
    primo = True
    for i in range(2, numero):
        divisoes_total += 1
        divisoes += 1
        if numero % i == 0:
            primo = False
            break
    if primo:
        primos.append(numero)

print("Números entre 1 e", n,":" )
print(primos)
print(f"Total de divisões realizadas: {divisoes_total} ")