# Todos os objetos nascem com o mesmo número de atributos de classe e de instancia.
# Atributos de instancia sao diferentes para cada objeto(cada objeto tem uma copia), ja os
# atributos de classe são compartilhados entre os objetos
# class Estudante:
#     escola = "UniFil"
#
#     def __init__(self, nome, numero):
#         self.nome = nome
#         self.numero = numero
#
#     def __str__(self):
#         return f'{self.nome} ({self.numero}) - {self.escola}'
#
# def mostrar_valores(*objs):
#     for obj in objs:
#         print(obj)
#
# joao = Estudante("Joao", 1)
# augusto = Estudante("Augusto", 2)
# mostrar_valores(joao, augusto)
#
# Estudante.escola = "Santa Maria"
# mirela = Estudante("Mirela", 10)
# mostrar_valores(joao, augusto, mirela)



# METODOS DE CLASSES E METODOS ESTATICO

# METODOS DE CLASSES
# Metodos de classe estao ligados a classe e nao ao objeto. Eles tem acesso ao estado da classe, pois recebem um
# parametro que aponta para a classe e nao para a instancia do objeto.
##################################################################################################################
# METODOS ESTATICOS
# Um metodo estatico nao recebe um primeiro argumento explicito, Ele tambem é um metodo vinculado a classe
# e nao ao objeto da classe. Este metodo nao pode acessar ou modificar o estado da classe. Ele esta presente
# em uma classe porque faz sentido que o metodo esteja presente na classe.

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18

# p = Pessoa(nome="Joao", idade=19)
# print(p.nome, p.idade)

p = Pessoa.criar_apartir_data_nascimento(2006 , 7, 6, "Joao")
print(p.nome, p.idade)

print(Pessoa.e_maior_de_idade(19))
print(Pessoa.e_maior_de_idade(13))

# O que são INTERFACES
# Uma INTERFACE define o que uma classe deve fazer e nao como

# CRIANDO CLASSES ABSTRATAS COM O MODULO ABC
# O QUE É ABC?
# ABC(abstract basic class). Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para
# definir as classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando
# classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado com @abstractmethod.

from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("ligando")

    def desligar(self):
        print("Desligando")

    @property
    def marca(self):
        return "PHILCO"

class ControleAR(ControleRemoto):
    def ligar(self):
        print("ligando AR")

    def desligar(self):
        print("Desligando AR")

    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controleAR = ControleAR()
controleAR.ligar()
controleAR.desligar()

print(controleAR.marca)