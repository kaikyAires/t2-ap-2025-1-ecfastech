def encontrar_palindromos_base(lista, base):
    resultado = []
    for numero in lista:
        convertido = encontrar_palindromos_base(str(numero), 10, base)
        if convertido == convertido[::-1]:
            resultado.append(numero)
    return resultado
