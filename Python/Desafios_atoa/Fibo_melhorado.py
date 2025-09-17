
def fibo_melhorado():
    while True:
        n = int(input("Informe um número natural não negativo: "))
        if n >= 0:
            a, b = 0, 1
            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()
            break
        else:
            print("Tente novamente")

fibo_melhorado()