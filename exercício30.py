# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela
# e preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo
# abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 0 - R$ 9.00

preço_pão = float(input("Digite o valor do pão: "))
print("Panificadora Pão de Ontem - Tabela de preços")
print("--------------------------------------------")
for quantidade in range(1,51):
    total = quantidade * preço_pão
    print(f"{quantidade} - R$ {total:.2f} ")