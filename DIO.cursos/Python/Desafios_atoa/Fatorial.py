n = int(input("Informe o valor de N: "))

def fatorial():
    if n == 0 or n == 1:
        return 1
    else:
        return  n * (n - 1)

print(f"Fatorial de {n} é igual a :{fatorial()}")