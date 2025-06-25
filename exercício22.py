# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais
# número ele é divisível.

numero = int(input("Digite um número inteiro: "))

if numero <= 1:
    print(f"O número {numero} não é primo. ")
else:
    divisores = []
    
    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)
    if len(divisores) == 0:
        print(f"O número {numero} é primo. ")
    else:
        print(f"O número {numero} não é primo. ")
        print(f"Ele é divisível por: {divisores} ")            