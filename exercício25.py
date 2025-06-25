 # Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a média de
 # idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
 # conforme a média calculada

n = int(input("Digite a quantidade de pessoas: "))
soma = 0

for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    soma += idade
media = soma / n

if media >= 0 and media <= 25:
    print(f"A média de idade é {media:.2f} anos. A turma é jovem.")
elif media <= 60:
    print(f"A média de idade é {media:.2f} anos. A turma é adulta.")
else:
    print(f"A media de idade é {media:.2f} anos. A turma é idosa.")        
