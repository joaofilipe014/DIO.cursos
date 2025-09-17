import textwrap

def menu():
    menu = """\n
    [v] = Visualizar extrato
    [d] = Depositar
    [s] = Sacar
    [nc] = Novo conta
    [nu] = Novo usuario
    [q] = Sair
    =>"""
    return input(textwrap.dedent(menu))

def depositar(saldo, extrato, valor,/):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("\n Sucesso!")
    else:
        print("Operation error, the informed value is invalid!")

    return saldo, extrato

def sacar(*, saldo, extrato, valor, numero_de_saques, limite, LIMITE_SAQUES):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operation error, you don't have enough money!")
    elif excedeu_saques:
        print("Operation error, withdrawal limit reached.")
    elif excedeu_limite:
        print("Operation error, the withdrawal amount exceeds the limit.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_de_saques += 1
        print("\n Saque realizado com sucesso!")
    else:
        print("Operation error, the informed value is invalid!")

    return saldo,extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n============ EXTRATO ================")
    print("Não foram relizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("========================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(apenas numeros): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Já existe um usúario com este CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento(dd/mm/aaaa): ")
    endereco = input("Informe o Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuario.append ({"Nome": nome, "Data Nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("USUARIO CRIADO COM SUCESSO!")
    return usuario

def criar_conta(numero_conta, agencia, usuarios):
    cpf = input("Informe o CPF do ususario: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia,"numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuario nao encontrado, fluxo encerrado!")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Iforme o valor do deposito: "))
            saldo, extrato = depositar(saldo, extrato, valor)

        elif opcao == 's':
            valor = float(input("Iforme o valor do saque: "))
            saldo ,extrato = sacar(
                saldo = saldo,
                extrato = extrato,
                valor = valor,
                numero_de_saques = numero_de_saques,
                limite = limite,
                LIMITE_SAQUES = LIMITE_SAQUES,
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato = extrato)
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_usuario(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'q':
            break
main()