class DigitoDisplay:
    representacoes = {
        '0': [' *** ', '*   *', '*   *', '*   *', ' *** '],
        '1': ['  *  ', ' **  ', '  *  ', '  *  ', ' *** '],
        '2': [' *** ', '    *', ' *** ', '*    ', ' *** '],
        '3': [' *** ', '    *', ' *** ', '    *', ' *** '],
        '4': ['*   *', '*   *', ' ****', '    *', '    *'],
        '5': ['*****', '*    ', '**** ', '    *', '**** '],
        '6': [' *** ', '*    ', '**** ', '*   *', ' *** '],
        '7': ['*****', '    *', '   * ', '  *  ', '  *  '],
        '8': [' *** ', '*   *', ' *** ', '*   *', ' *** '],
        '9': [' *** ', '*   *', ' ****', '    *', ' *** '],
        'A': [' *** ', '*   *', '*****', '*   *', '*   *'],
        'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
        'C': [' *** ', '*    ', '*    ', '*    ', ' *** '],
        'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
        'E': ['*****', '*    ', '**** ', '*    ', '*****'],
        'F': ['*****', '*    ', '**** ', '*    ', '*    ']
    }

    def __init__(self, valor):
        self.representacao = DigitoDisplay.representacoes.get(valor.upper(), ['     ']*5)


class DisplayDigital:
    def __init__(self, num_digitos):
        self.num_digitos = num_digitos
        self.digitos = []

    def exibir_numero(self, numero):
        if len(numero) > self.num_digitos:
            print("Número muito grande para o display")
            return
        self.digitos = [DigitoDisplay(c) for c in numero]

    def renderizar_display(self):
        for linha in range(5):
            for digito in self.digitos:
                print(digito.representacao[linha], end=' ')
            print()


# Exemplo:
display = DisplayDigital(4)
display.exibir_numero('1A3F')
display.renderizar_display()
