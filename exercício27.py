# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e
# a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input("Digite a quantidade de turmas: "))
soma = 0

for i in range(1, turmas + 1):
    while True:
        alunos = int(input(f"Digite a quantidade de alunos na turma {i} (maxímo 40): "))
        if alunos <= 40:
            soma += alunos
            break
        else:
            print("quantidade inválida! A turma não pode ter mais de 40 alunos. ")
media = soma / turmas
print(f"A média de alunos por turma é: {media}")               