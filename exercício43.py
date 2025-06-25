cardapio = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com Ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}

total = 0

while True:
    codigo = int(input("Digite o código do item (0 para encerrar): "))
    if codigo == 0:
        break
    if codigo in cardapio:
        quantidade = int(input("Quantidade: "))
        nome, preco = cardapio[codigo]
        subtotal = preco * quantidade
        total += subtotal
        print(f"{nome}: R$ {subtotal:.2f}")
    else:
        print("Código inválido!")

print(f"Total a pagar: R$ {total:.2f}")
