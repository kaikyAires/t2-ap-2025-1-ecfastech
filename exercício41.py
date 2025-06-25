divida = float(input("Digite o valor da dívida: R$ "))
parcelas_juros = {1: 0, 3: 10, 6: 15, 9: 20, 12: 25}

print("\nValor da Dívida | Juros | Parcelas | Valor da Parcela")
print("-" * 55)

for parcelas, juros in parcelas_juros.items():
    valor_juros = divida * (juros / 100)
    total = divida + valor_juros
    valor_parcela = total / parcelas
    print(f"R$ {total:.2f}         {juros}%       {parcelas}       R$ {valor_parcela:.2f}")
