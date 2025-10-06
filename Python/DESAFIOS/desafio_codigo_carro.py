class Carro:
    def __init__(self, modelo, ano_fabricacao, ano_atual):
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao
        self.ano_atual = ano_atual

    def verificar_aptidao_carro(self):
        idade_carro = self.ano_atual - self.ano_fabricacao
        return idade_carro

        # TODO: Verifique se o carro está apto com base na idade

    def exibir_mensagem(self, idade_carro):
        if idade_carro <= 10:
            return f'{self.modelo}: Apto'
        else:
            return f'{self.modelo}: Nao apto'


def main():
    modelo = input()
    ano_fabricacao = int(input())
    ano_atual = int(input())

    # TODO: Chame a função para verificar a aptidão do carro
    resultado = Carro(modelo, ano_fabricacao, ano_atual)
    idade_carro = resultado.verificar_aptidao_carro()
    print(resultado.exibir_mensagem(idade_carro))


if __name__ == "__main__":
    main()