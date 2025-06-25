def copiar_arquivo(origem, destino):
    try:
        with open(origem, 'r') as arquivo_origem:
            conteudo = arquivo_origem.read()
        with open(destino, 'w') as arquivo_destino:
            arquivo_destino.write(conteudo)
    except FileNotFoundError:
        print("Arquivo de origem não encontrado!")
