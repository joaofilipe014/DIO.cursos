n = int(input("Digite um número inteiro e não negativo: "))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(n):
    print(fibonacci(i), end=" ")
