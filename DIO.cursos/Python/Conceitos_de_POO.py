# class Bicicleta:
#     def __init__(self, cor, modelo, ano, valor):
#         self.cor = cor
#         self.modelo = modelo
#         self.ano = ano
#         self.valor = valor
#
#     def buzinar(self):
#         print("PRIPRIPRIPRI")
#
#     def parar(self):
#         print("Parando...")
#         print("biclieta parada!")
#
#     def correr(self):
#         print("Correndo...")


    # def __str__(self):
    #     return f"Cor: {self.cor}, Modelo: {self.modelo},
    #     Ano: {self.ano}, Valor: {self.valor}"
#
    # def __str__(self):
    #     return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
#
#
#
# speed = Bicicleta("Preta", "Gy25", 2019, 61000)
# speed.buzinar()
# speed.correr()
# speed.parar()
# print(speed.cor, speed.modelo, speed.ano, speed.valor)
# print("---------------------------------------")
# mountain = Bicicleta("Vermelha", "Mountain", 2020, 100000)
# mountain.buzinar() # Bicicleta.buzinar(mountain)
# mountain.correr()
# mountain.parar()
# print(mountain.cor, mountain.modelo, mountain.ano, mountain.valor)
# print(mountain)

# metodo construtor
# class Carro:
#     def __init__(self, marca, modelo, ano, valor):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#         self.valor = valor
# # metodo destrutor
#     def __del__(self): # nao é necessario, pois o Python, executa o metodo destrutor automaticamente
#         # quando um onjeto(instancia) é destruida
#         print("Objeto coletado")

# Sintaxe da Herança em PY
#Herança simples
# class A:
#     pass
# class B(A):
#     pass
#
# # Herança múltipla
# class C(A,B):
#     pass

# Exemplo - Herança simples
# class Veiculo:
#     def __init__(self, cor, placa, nmr_rodas):
#         self.cor = cor
#         self.placa = placa
#         self.nmr_rodas = nmr_rodas
#
#     def ligar_motor(self):
#         print("Motor ligado!")
#
#     def __str__(self):
#         return self.cor
#
# class Carro(Veiculo):
#     pass
#
# class Moto(Veiculo):
#     pass
#
# class Caminhao(Veiculo):
#     def __init__(self, cor, placa, nmr_rodas, carregado):
#         super().__init__(cor, placa, nmr_rodas)
#         self.carregado = carregado
#     def carga(self):
#        print(f"{'Sim' if self.carregado else 'Não'} está carregado")
#
# moto = Moto("Vermelha", "ABC-12B4", 2)
# moto.ligar_motor()
#
# carro = Carro("Preta", "ABC-12A4", 4)
# carro.ligar_motor()
#
# caminhao = Caminhao("Branca", "ABC-123", 12, True)
# caminhao.ligar_motor()
# caminhao.carga()
# print(caminhao)

# Exemplo herança Múltipla
class Animal:
    def __init__(self, nmr_patas):
        self.nmr_patas = nmr_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Aves(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    # def __str__(self):
    #     return 'ave 14'

class Mamifero(Animal):
    def __init__(self, cor_pelos, **kw):
        self.cor_pelos = cor_pelos
        super().__init__(**kw)

    # def __str__(self):
    #     return 'mamifero 14'

class Cachorro(Mamifero):
    pass

class Ornitorrinco(Mamifero, Aves):
    def __init__(self, cor_bico, cor_pelos, nmr_patas):
        # print(Ornitorrinco.__mro__)
        super().__init__(cor_bico = cor_bico, cor_pelos = cor_pelos, nmr_patas = nmr_patas)

    # def __str__(self):
    #     return 'ornitorrinco 14'
cachorro = Cachorro(nmr_patas=4, cor_pelos="preto e branco")
# print(cachorro)

ornitorrinco = Ornitorrinco(nmr_patas = 4,cor_pelos = "marrom", cor_bico = "Acinzentado")
print(ornitorrinco)