def anexar_conteudo(nome_arquivo, conteudo_extra):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(conteudo_extra)
