def calcular_fatorial(n):
    if n < 0:
        return "Erro: número negativo"
    if n == 0 or n == 1:
        return 1
    return n * calcular_fatorial(n - 1)
