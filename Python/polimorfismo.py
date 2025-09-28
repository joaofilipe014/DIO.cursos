# print(len("python"))
# print(len([3,4,5,6,7,8,9,5,32]))

class Passaro():
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
