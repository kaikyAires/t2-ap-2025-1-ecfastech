def validar_numeros_base(lista, base):
    mapa = '0123456789ABCDEF'[:base]
    validos = []
    for numero in lista:
        numero = numero.upper()
        if all(char in mapa for char in numero):
            validos.append(numero)
    return validos
