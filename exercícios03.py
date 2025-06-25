# Faça um programa que leia e valide as seguintes informações:
# a) Nome: maior que 3 caracteres;
# b) Idade: entre 0 e 150;
# c) Salário: maior que zero;
# d) Sexo: 'f' ou 'm';
# e) Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).

# Validação do nome

while True:
    nome = input("Digite seu nome (mais de 3 caracteres): ")
    if len(nome) > 3:
        break
    else:
        print("Nome inválido! Deve ter mais de 3 caracteres.")

# Validação da idade

while True:
    idade = int(input("Digite sua idade (entre 0 e 150): "))
    if 0 <= idade <= 150:
        break
    else:
        print("Idade inválida! Deve estar entre 0 e 150.")

# Validação do salário

while True:
    salario = float(input("Digite seu salário (maior que 0): "))
    if salario > 0:
        break
    else:
        print("Salário inválido! Deve ser maior que zero.")

# Validação do sexo

while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Sexo inválido! Digite apenas 'f' ou 'm'.")

# Validação do estado civil
while True:
    estado_civil = input("Digite seu estado civil ('s'=solteiro, 'c'=casado, 'v'=viúvo, 'd'=divorciado): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil inválido! Digite apenas 's', 'c', 'v' ou 'd'.")

# Resultado final
print("\nInformações válidas cadastradas com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {estado_civil}")