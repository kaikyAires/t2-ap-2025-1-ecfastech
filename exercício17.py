# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

numero = int(input("Digite um número inteiro: "))
fatorial = 1
while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1
print(f"O fatorial desse número é {fatorial }")