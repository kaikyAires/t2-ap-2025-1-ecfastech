def somar_numeros_arquivo(nome_arquivo):
    total = 0
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                try:
                    total += int(linha.strip())
                except ValueError:
                    continue
        return total
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return 0
