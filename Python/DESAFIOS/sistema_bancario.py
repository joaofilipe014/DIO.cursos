menu = """
[v] = Visualizar extrato
[d] = Depositar
[s] = Sacar
[q] = Sair
=>"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "v":
        print("\n============ EXTRATO ================")
        print("Não foram relizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("========================================")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operation error, the informed value is invalid!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operation error, you don't have enough money!")

        elif excedeu_limite:
            print("Operation error, the withdrawal amount exceeds the limit.")

        elif excedeu_saques:
            print("Operation error, withdrawal limit reached.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
    elif opcao == "q":
        break

    else:
        print("Operation error, the informed value is invalid!")