# Faça um programa que leia 5 números e informe o maior número

maior = float(input("Digite o maior número: "))

for i in range(6):
    numero = float(input(f"Digite o {i} número: "))
    if numero > maior:
        maior = numero
print(f"O maior número é {maior} ")        