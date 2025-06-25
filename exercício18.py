# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma
# dos valores.

n = int(input("Digite a quantidade de N: "))
numero = float(input("Digite o 1° número: "))
soma = numero
maior = numero
menor = numero

for i in range(2, n + 1):
    numero = float(input("Digite o {i}° numero: "))
    soma += numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f"A soma dos números é {soma} ")
print(f"O número maior é {maior }")
print(f"O número menor é {menor }")        
