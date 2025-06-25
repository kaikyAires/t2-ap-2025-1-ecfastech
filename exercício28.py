# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor
# médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um.

cDS = int(input("Digite a quantidade de CDs: "))
soma = 0
for i in range(1, cDS + 1):
    valor = float(input(f"Digite o valor do  CD {i}: R$ "))
    soma += valor
media = soma / cDS
print(f"O valor total investido pelo colecionador em sua coleção é:R${soma:.3f} ")
print(f"O valor médio gasto por CD é:R${media:.3f}")