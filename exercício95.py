def converter_base(numero_str, base_origem, base_destino):
    mapa = '0123456789ABCDEF'

    def para_decimal(num_str, base):
        num_str = num_str.upper()
        decimal = 0
        for i, digito in enumerate(reversed(num_str)):
            decimal += mapa.index(digito) * (base ** i)
        return decimal

    def de_decimal(decimal, base):
        if decimal == 0:
            return '0'
        resultado = ''
        while decimal > 0:
            resultado = mapa[decimal % base] + resultado
            decimal //= base
        return resultado

    decimal = para_decimal(numero_str, base_origem)
    return de_decimal(decimal, base_destino)
