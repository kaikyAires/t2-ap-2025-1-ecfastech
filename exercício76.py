def desenhar_triangulo(altura, tipo):
    for i in range(1, altura + 1):
        if tipo == 'esquerda':
            print('*' * i)
        elif tipo == 'direita':
            print(' ' * (altura - i) + '*' * i)
        elif tipo == 'centralizado':
            print(' ' * (altura - i) + '*' * (2 * i - 1) + ' ' * (altura - i))
        else:
            print("Tipo inválido!")

desenhar_triangulo(5, 'centralizado')
