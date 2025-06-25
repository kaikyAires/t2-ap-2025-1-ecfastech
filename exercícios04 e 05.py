# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
# crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A
# ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
população_A = 80000
população_B = 200000
taxa_A = 0.03
taxa_B = 0.015
anos = 0

while população_A < população_B:
    população_A = população_A * taxa_A
    população_B = população_B * taxa_B
    anos = + 1
print(f"Será nescessário {anos} anos para que a população do país A ultrapasse ou iguale a do páis B. ")

repetir = "s"
while repetir == "s" or repetir == "S":
    população_A = 0
    while população_A <= 0:
        população_A = float(input("Informe a população do páis A: "))
        if população_A <= 0:
            print("População deve ser maior que sero: ")
    
    população_B = 0
    while população_B <= 0:
        população_B = float(input("Informe a população do páis B: "))
        if população_B <= 0:
            print("População deve ser maior que zero: ")

    taxa = 0
    while taxa_A <= 0:
        taxa_A = float(input("Informe a taxa de crescimento do páis A (em %):"))    
        if taxa_A <= 0:
            print("Taxa deve ser maior que zero. ")

    taxa_B = 0
    while taxa_B <= 0:
        taxa_B = float(input("Informe a taxa de crescimento do páis B (em %): "))
        if taxa_B <= 0:
            print("Taxa deve ser maior que zero. ")
    if população_A >= população_B:
        print("A população do páis A já é maior ou igual a do Páis B. ")
    else:
        anos = 0
        taxa_A = taxa_A / 100
        taxa_B = taxa_B / 100

        while população_A < população_B:
            população_A = população_A + (população_A * taxa_A)
            população_B = população_B + (população_B * taxa_B)
            anos += 1
        print("Serão nescessários", anos, "anos para que a população do páis A ultrapasse ou iguale a do páis B.")

    repertir = input("Deseja fazer outro cálculo? (s/n): ")
