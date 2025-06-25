# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo
# compreendido por eles

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

# Verifica qual é o menor e o maior
menor = min(n1, n2)
maior = max(n1, n2)

print(f"Números no intervalo entre {menor} e {maior}:")

for i in range(menor + 1, maior):
    print(i)