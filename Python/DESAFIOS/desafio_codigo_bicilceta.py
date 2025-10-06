class BicicletaInterna:
    def __init__(self, modelo, nivel_bateria):
        self.modelo = modelo
        self.nivel_bateria = nivel_bateria

    def calcular_distancia(self):
       distancia = self.nivel_bateria * 0.5
       return distancia

    # TODO: Calcule a distância estimada com base no nível de bateria

    def obter_mensagem(self):
        return f'{self.modelo}: Distancia estimada = {self.calcular_distancia() : .1f} km'



# TODO: Retorne a mensagem formatada com o modelo e a distância




def main():
    modelo = input()
    nivel_bateria = int(input())

    bicicleta = BicicletaInterna(modelo, nivel_bateria)
    print(bicicleta.obter_mensagem())


if __name__ == "__main__":
    main()