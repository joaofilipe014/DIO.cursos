# O Encapsulamento, é uma forma de proteger certos dados, n~so deixando que ele seja acessado de forma normal igual acessa um dado
# público, necessita de um método para acessa-lo, como neste caso o def mostrar_saldo

# class Conta:
#     def __init__(self, nmr_agencia, saldo =0):
#         self._saldo = saldo # saldo aqui é privado pela convenção de usar o underline antes do nome (_saldo)
#         self.nmr_agencia = nmr_agencia
#
#     def depositar(self, valor):
#         self._saldo += valor
#
#     def sacar(self, valor):
#         self._saldo -= valor
#
#     def mostrar_saldo(self):
#         return self._saldo
#
# conta = Conta("1003",100)
# conta.depositar(100)
# print(conta.nmr_agencia)
# print(conta.mostrar_saldo())

### PROPERTY
# class Foo:
#     def __init__(self, x = None):
#         self._x = x
#
#     @property
#     def x (self):
#         return self._x or 0
#
#     @x.setter
#     def x (self, value):
#         _x = self._x or 0
#         _value = value or 0
#         self._x += _value
#
#     @x.deleter
#     def x(self):
#         self._x = -1
#
# foo = Foo(10)
# print(foo.x)
# foo.x = 10
# print(foo.x)
# del foo.x
# print(foo.x)

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa('joão', 2006)

print(f"nome: {pessoa.nome} \t idade: {pessoa.idade}v ")