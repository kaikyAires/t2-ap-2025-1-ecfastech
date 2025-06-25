# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O
# usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:


for i in range(1, 11):
    resultado = 3 * i
    print(f"3 x {i} = {resultado}")