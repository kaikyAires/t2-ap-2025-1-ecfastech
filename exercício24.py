# Faça um programa que calcule e mostre a média aritmética de N notas.

n = int(input("Digite a quantidade de notas: "))
soma = 0

for i in range(n):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma += nota

media = soma / n
print(f"A média artmética das {n} notas é: {media:.2f}")