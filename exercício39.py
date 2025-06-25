maior_altura = 0
menor_altura = float('inf')
aluno_mais_alto = 0
aluno_mais_baixo = 0

for _ in range(10):
    numero = int(input("Número do aluno: "))
    altura = float(input("Altura (em cm): "))

    if altura > maior_altura:
        maior_altura = altura
        aluno_mais_alto = numero

    if altura < menor_altura:
        menor_altura = altura
        aluno_mais_baixo = numero

print("\n--- Resultado ---")
print(f"Aluno mais alto: Nº {aluno_mais_alto} com {maior_altura} cm")
print(f"Aluno mais baixo: Nº {aluno_mais_baixo} com {menor_altura} cm")