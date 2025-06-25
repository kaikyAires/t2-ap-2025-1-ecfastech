# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série
# até que o valor seja maior que 500.

a = 0
b = 1

print("Série de Fibonacci até ultrapassar 500:")

while a <= 500:
    print(a, end=" ")  
    proximo = a + b
    a = b
    b = proximo