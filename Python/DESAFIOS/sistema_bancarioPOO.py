from datetime import datetime
from abc import ABC, abstractmethod
import textwrap

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n###Não foi possivel completar a operação, saldo insuficiente.###")
        elif valor > 0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso.")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n Operação realizada com sucesso.")
        else:
            print("\n A operação falhou o valor informado é inválido.")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=1000, limite_saques=5):
        super().__init__(numero, cliente)
        self._limite = limite
        self.limite_saques = limite_saques

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        numero_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == Saque.__name__]
        )
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n Operação falhou! O valor de saque excedeu o limite.")
        elif excedeu_saques:
            print("\n Operação falhou número máximo de saques excedido!")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
               Agencia: \t{self.agencia}
               C/C: \t{self._numero}
               Titular: \t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def contas(self):
        return self._contas


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def menu():
    menu1 = """\n
        [v] = Visualizar extrato
        [d] = Depositar
        [s] = Sacar
        [nc] = Nova conta
        [nu] = Novo usuário
        [lc] = Listar contas
        [q] = Sair
        =>"""
    return input(textwrap.dedent(menu1))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [c for c in clientes if c.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente nao possui conta.")
        return None
    return cliente.contas[0]  # FIXME: não permite cliente escolher conta


def depositar(clientes):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente nao encontrado.")
        return None

    valor = float(input("\n Informe o valor do deposito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return None

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente nao encontrado.")
        return None
    valor = float(input("\n Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return None

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente nao encontrado.")
        return None

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return None

    print("============EXTRATO============")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas operações"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\t R${transacao['valor']:.2f}"
    print(extrato)
    print(f"\nSaldo:\n\tR${conta.saldo:.2f}")
    print("================================")


def criar_cliente(clientes):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n Já existe um cliente com esse CPF.")
        return None
    nome = input("\n Informe o nome completo do cliente: ")
    data_nascimento = input("\n Informe a data de nascimento: ")
    endereco = input("\n Informe o logradouro, nmr-bairro-cidade/sigla estado: ")

    cliente = PessoaFisica(cpf=cpf, nome=nome, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)

    print("\n=== CLIENTE CRIADO COM SUCESSO ===")


def criar_conta(_numero_conta, clientes, contas):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente nao encontrado. Opção de criar conta encerrada.")
        return None

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=_numero_conta)
    contas.append(conta)
    cliente.adicionar_conta(conta)


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "v":
            exibir_extrato(clientes)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break


if __name__ == "__main__":
    main()
