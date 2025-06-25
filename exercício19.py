# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input("Digite a quantidade de números: "))

def verficacao(numero):
    while True:
        numero = float(input("números entre 0 e 1000: "))
        if 0 <= numero <= 1000:
            return numero
        else:
            print("Número inválido. Digite um número entre 0 e 1000. ")

numero = verficacao("Digite o 1° número entre (0 e 1000): ")
soma = numero 
maior = numero
menor = numero

for i in range(2, n + 1):
    numero = verficacao(f"Digite o {i}° entre (0 e 1000): ")
    soma += numero

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print(f"A soma dos números é {soma}. ")
print(f"O maior número é {maior}. ")
print(f"O menor número é {menor}. ")