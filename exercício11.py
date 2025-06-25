# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles.

# Altere o programa anterior para mostrar no final a soma dos números



n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

menor = min(n1, n2)
maior = max(n1, n2)

print(f"Números no intervalo entre {menor} e {maior}:")

soma = 0
for i in range(menor + 1, maior):
    print(i)
    soma += i

print(f"Soma dos números do intervalo: {soma}")