# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
        return resultado
while True:
    numero = input("Digite um número inteiro e positivo menor que 16 (ou 'sair' para encerrar):" )
    if numero.lower() == "sair":
        print("Encerrando o programa. ")
        break
    if not numero.isdigit():
        print("Entrada inválida. Por favor, insira um número inteiro. ")
        continue
    numero = int(numero)
    if numero <= 0:
        print("Por favor, insira uma número positivo. ")
    elif numero > 16:
        print("Por favor, digite um número menor que 16. ")
    else:
        print(f"O fatorial de {numero} é {fatorial(numero)}. ")        