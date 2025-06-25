from exercício95 import converter_base


def realizar_operacao_base(num1_str, num2_str, base_origem, operacao, base_destino):
    n1 = int(converter_base(num1_str, base_origem, 10))
    n2 = int(converter_base(num2_str, base_origem, 10))

    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        if n2 == 0:
            return "Erro: divisão por zero"
        resultado = n1 // n2
    else:
        return "Operação inválida"

    return converter_base(str(resultado), 10, base_destino)
