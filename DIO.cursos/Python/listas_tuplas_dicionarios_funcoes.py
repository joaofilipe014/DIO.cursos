# frutas = ("laranja", " maçã", "uva")
# print(frutas)
#
# frutas = []
# print(frutas)
#
# letras = list("Python")
# print(letras)
#
# numeros = list(range(10))
# print(numeros)
#
# carro = ["Ferrari", "F8", 4200000, 2020, 2900, "PR", True]
# print(carro)

# matriz = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]
#           ]
# # Acessa a primeira linha
# print(matriz[0])
# # acessa o primeiro elemento da primeira linha
# print(matriz[0][0])
# # acessa o último item da primeira linha
# print(matriz[0][-1])
# # acessa a última linha da primeira coluna, e o ultimo item da ultima linha
# print(matriz[-1][-1])

# lista = list(range(61))
# # compressão de lista
# lista_pares = [numero for numero in lista if numero % 2 == 0]
# print(lista_pares)
# lista_quadrado = [numero ** 2 for numero in lista]
# print(lista_quadrado)

# ex.append() = adiciona item a lista
# ex.clear() = limpa a lista
# ex.copy() = retorna uma lista igual com uma INSTANCIA diferente
# ex.count() = conta quantas vezes o item aparece na lista
# ex.extend() = adiciona uma lista de itens dentro de outra lista, só que diferentemente de append o extend mergeia as lista para que nao fiquem assim [[7, 8, 9, 0]0,1,2,3,4]
# ex.index() = mostra a posição da primeira aparição de um certo item na lista
# ex.pop() = serve para remover o último elemento da lista, caso voce nao forneça um argumento
# ex.remove() = serve para remover o objeto especificado da lista, da para apagar a propria lista
# ex.reverse() = pega a lista e a inverte
# ex.sort() = ordena a lista
# print(len(ex)) = retorna a quantidade de elementos da lista
# n = [n ** 2 if n > 6 else n for n in range(10) if n % 2 == 0]
# print(n)

########################################################
# TUPLAS
carros = ("gol")
print(isinstance(carros, tuple))