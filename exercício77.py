def combinar_listas(*listas):
    combinada = []
    for lista in listas:
        combinada.extend(lista)
    return combinada

# Exemplo:
print(combinar_listas([1,2], ['a','b'], [3,4]))
