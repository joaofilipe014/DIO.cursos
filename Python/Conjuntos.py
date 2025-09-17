# set elimina itens duplicados dentro de uma lista
# quando falamos em set é importante lembrar de conjuntos matemáticos

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {5, 6, 7, 8, 9}

# conjunto_a.union(conjunto_b) faz a uniao de dois conjuntos
print(conjunto_a.union(conjunto_b))

# conjunto_a.intersection(conjunto_b) faz a intersecao de dois conjuntos, apenas os elementos que estao em ambos
print(conjunto_a.intersection(conjunto_b))

# conjunto_a.difference(conjunto_b) faz a diferenca entre dois conjuntos, apenas os elementos que estao em a, mas nao em b
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# conjunto_a.symmetric_difference(conjunto_b) retorna os elementos que estao em a ou b mas nao em ambos
print(conjunto_a.symmetric_difference(conjunto_b))

# conjunto_a.issubset(conjunto_b) retorna se os valores de a estao dentro de b e vice versa
print(conjunto_a.issubset(conjunto_b))

# conjunto_a.issuperset(conjunto_b) retorna se os valores de a estao dentro de b e vice versa
print(conjunto_a.issuperset(conjunto_b))

# conjunto_a.isdisjoint(conjunto_b) retorna se os valores de a e b nao estao em comum
print(conjunto_a.isdisjoint(conjunto_b))

sorteio = {1, 23}
# sorteio.add(3) adiciona um elemento ao conjunto, se o elemento ja existir ele é ignorado
print(sorteio)
sorteio.add(3)
print(sorteio)

numero = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
# numero.discard(10) remove um elemento do conjunto, se o elemento nao existir ele ignora
print(numero)
numero.discard(10)
print(numero)
numero.discard(10)
print(numero)
